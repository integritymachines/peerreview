#!/usr/bin/env python3
"""Two independent, budget-capped LLM assessments; offline comparison."""
import argparse
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
FAMILIES = {"randomized", "adjustment", "instrumental_variables", "difference_in_differences",
            "regression_discontinuity", "synthetic_control", "structural_selection",
            "graphical", "longitudinal_g_methods", "partial_identification", "other"}
FITS = {"appropriate", "mismatch", "indeterminate"}

def read_jsonl(path):
    rows = [json.loads(t) for t in Path(path).read_text(encoding="utf-8").splitlines() if t.strip()]
    ids = [r.get("paper_id") for r in rows]
    if not all(ids) or len(set(ids)) != len(ids):
        raise ValueError("paper_id values must be unique and nonempty")
    return rows

def validate(kind, result):
    if not isinstance(result, dict):
        raise ValueError("JSON object required")
    if kind == "signature":
        s = result["signature"]
        if set(s) != {"R", "F", "D"} or any(type(v) not in (int,float) or not 0 <= v <= 1 for v in s.values()):
            raise ValueError("R,F,D must lie in [0,1]")
        families = result["recommended_frameworks"]
    else:
        if result["fit"] not in FITS:
            raise ValueError("Unknown fit verdict")
        if type(result.get("materially_better_alternative")) is not bool:
            raise ValueError("Expected boolean materially_better_alternative")
        if result["fit"] == "mismatch" and not result.get("reason"):
            raise ValueError("Mismatch requires an explicit justification")
        families = result["framework_used"]
        used = result["preferred_frameworks"]
        if not isinstance(used,list) or not set(used) <= FAMILIES:
            raise ValueError("Unknown preferred family")
    if not isinstance(families,list) or not set(families) <= FAMILIES:
        raise ValueError("Unknown framework family")
    return result

def get_text(reply):
    pieces = [c.get("text","") for item in reply.get("output",[]) for c in item.get("content",[]) if c.get("type") == "output_text"]
    if not pieces:
        raise ValueError("Model returned no output_text")
    return "\n".join(pieces)

def ask_model(prompt, source, model, token_cap):
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY required; no model inference performed")
    payload = {"model":model, "instructions":prompt, "input":source+"\nReturn only the required JSON.",
               "text":{"format":{"type":"json_object"}}, "max_output_tokens":token_cap, "store":False}
    req = urllib.request.Request("https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=120) as resp:
            out = json.load(resp)
    except urllib.error.HTTPError as ex:
        raise RuntimeError(f"API HTTP {ex.code}: {ex.read().decode(errors='replace')[:250]}") from ex
    return json.loads(get_text(out)), out.get("usage",{})

def read_source(manifest, relative, limit):
    filename = (Path(manifest).resolve().parent / relative).resolve()
    content = filename.read_text(encoding="utf-8")
    if len(content) > limit:
        raise ValueError(f"{filename}: source exceeds {limit} chars; provide a faithful shorter extract, never silently truncate")
    if len(content.strip()) < 100:
        raise ValueError(f"{filename}: insufficient source text")
    return content

def run(args):
    if not args.execute:
        raise SystemExit("No API calls made. Supply --execute explicitly.")
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("No API calls made. OPENAI_API_KEY is missing.")
    if not 1 <= args.limit <= 5:
        raise ValueError("Hard pilot limit: 1 to 5 papers")
    manifest = read_jsonl(args.manifest)
    sig_prompt = (ROOT/"mdci/signature-lite.txt").read_text(encoding="utf-8")
    peer_prompt = (ROOT/"review-lite.txt").read_text(encoding="utf-8")
    output = Path(args.output)
    output.parent.mkdir(parents=True,exist_ok=True)
    done = {r["paper_id"] for r in read_jsonl(output)} if output.exists() and output.stat().st_size else set()
    for row in manifest[:args.limit]:
        paper_id = row["paper_id"]
        if paper_id in done:
            print("Skipping completed", paper_id, file=sys.stderr)
            continue
        dossier = read_source(args.manifest,row["dossier"],args.max_chars)
        paper = read_source(args.manifest,row["paper"],args.max_chars)
        # Independently constructed API requests, without shared history.
        sig,usage_s = ask_model(sig_prompt,dossier,args.model,args.max_output_tokens)
        validate("signature",sig)
        review,usage_r = ask_model(peer_prompt,paper,args.model,args.max_output_tokens)
        validate("review",review)
        item = {"paper_id":paper_id,"signature":sig,"review":review,
                "usage":{"signature":usage_s,"review":usage_r},"model":args.model}
        with output.open("a",encoding="utf-8") as dest:
            dest.write(json.dumps(item,ensure_ascii=False)+"\n")
        print("Completed",paper_id,file=sys.stderr)
    print(output)

def compare(rows):
    joined = []
    for item in rows:
        sig = validate("signature",item["signature"])
        rev = validate("review",item["review"])
        predicted = set(sig["recommended_frameworks"])
        used = set(rev["framework_used"])
        preferred = set(rev["preferred_frameworks"])
        joined.append({"paper_id":item["paper_id"],"signature":sig["signature"],
                       "review_fit":rev["fit"],"used":sorted(used),
                       "predicted":sorted(predicted),"review_preferred":sorted(preferred),
                       "supports_used":bool(predicted & used) if predicted and used else None,
                       "recommended_overlap":bool(predicted & preferred) if predicted and preferred else None})
    eligible = [r for r in joined if r["supports_used"] is not None and r["review_fit"]!="indeterminate"]
    agreement = [bool(not r["supports_used"]) == (r["review_fit"]=="mismatch") for r in eligible]
    return {"papers":len(joined),
            "review_appropriate":sum(r["review_fit"]=="appropriate" for r in joined),
            "review_mismatch":sum(r["review_fit"]=="mismatch" for r in joined),
            "review_indeterminate":sum(r["review_fit"]=="indeterminate" for r in joined),
            "comparison_eligible":len(eligible),
            "binary_agreement":sum(agreement)/len(agreement) if agreement else None,
            "warning":"LLM reviewer agreement is not ground truth. No prior mismatch prevalence assumed.",
            "rows":joined}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command",required=True)
    a = sub.add_parser("run")
    a.add_argument("--manifest",required=True)
    a.add_argument("--output",default="results.jsonl")
    a.add_argument("--limit",type=int,default=2)
    a.add_argument("--model",default="gpt-4.1-mini")
    a.add_argument("--max-output-tokens",type=int,default=1400)
    a.add_argument("--max-chars",type=int,default=25000)
    a.add_argument("--execute",action="store_true")
    b = sub.add_parser("compare")
    b.add_argument("--results",required=True)
    b.add_argument("--output",default="comparison.json")
    args = p.parse_args()
    if args.command=="run":
        run(args)
    else:
        report = compare(read_jsonl(args.results))
        Path(args.output).write_text(json.dumps(report,indent=2),encoding="utf-8")
        print(json.dumps({k:v for k,v in report.items() if k!="rows"},indent=2))

if __name__=="__main__":
    main()
