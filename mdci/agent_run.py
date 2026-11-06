#!/usr/bin/env python3
"""Prepare isolated assessment inputs and collect their frozen responses; no API key.

An operator in a host with fresh-context agents executes each request once.
This module does not pretend that exporting requests performs inference.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

try:
    from . import run
except ImportError:
    import run


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def request_hash(request):
    return digest(json.dumps({k: v for k, v in request.items() if k != 'request_hash'}, sort_keys=True, ensure_ascii=False))


def prepare(manifest, directory, limit=5):
    if not 1 <= limit <= 5:
        raise ValueError('Hard pilot limit: 1 to 5 papers')
    directory = Path(directory)
    # Refuse to overwrite a run, including responses from a partially completed run.
    directory.mkdir(parents=True, exist_ok=False)
    requests = []
    try:
        for row in run.read_jsonl(manifest)[:limit]:
            paper_id = row['paper_id']
            if not re.fullmatch(r'[A-Za-z0-9_-]+', paper_id):
                raise ValueError('Paper IDs must be safe opaque filenames')
            for branch, source_key, prompt_file in [
                ('signature', 'dossier', 'signature-lite.txt'),
                ('review', 'paper', 'review-lite.txt'),
            ]:
                source = run.read_source(manifest, row[source_key], 25000)
                instructions = (run.ROOT / prompt_file).read_text(encoding='utf-8')
                request = {'paper_id': paper_id, 'branch': branch,
                           'instructions': instructions, 'source': source,
                           'source_sha256': digest(source), 'prompt_sha256': digest(instructions)}
                request['request_hash'] = request_hash(request)
                requests.append(request)
        for request in requests:
            path = directory / request['branch'] / (request['paper_id'] + '.json')
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps(request, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            path.chmod(0o400)
        index = [{k: r[k] for k in ('paper_id', 'branch', 'request_hash')} for r in requests]
        (directory / 'index.json').write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
        print(f'Prepared {len(requests)} requests. No inference performed.')
    except Exception:
        # Retain an explicit failed preparation, never quietly reuse a partial directory.
        (directory / 'PREPARATION_FAILED').touch()
        raise


def collect(requests, responses, output, execution_label):
    requests, responses, output = Path(requests), Path(responses), Path(output)
    if (requests / 'PREPARATION_FAILED').exists():
        raise ValueError('Request preparation failed')
    index = json.loads((requests / 'index.json').read_text(encoding='utf-8'))
    if not index or len(index) > 10:
        raise ValueError('Expected 1 to 5 assessment pairs')
    results = {}
    audit = []
    for item in index:
        paper_id, branch = item['paper_id'], item['branch']
        request = json.loads((requests / branch / (paper_id + '.json')).read_text(encoding='utf-8'))
        if request_hash(request) != item['request_hash'] or request['request_hash'] != item['request_hash']:
            raise ValueError('Changed request: ' + paper_id + '/' + branch)
        if digest(request['source']) != request['source_sha256'] or digest(request['instructions']) != request['prompt_sha256']:
            raise ValueError('Changed source or prompt')
        envelope = json.loads((responses / branch / (paper_id + '.json')).read_text(encoding='utf-8'))
        for key in ('paper_id', 'branch', 'request_hash'):
            if envelope.get(key) != item[key]:
                raise ValueError('Response identity mismatch: ' + paper_id + '/' + branch)
        result = run.validate(branch, envelope['result'])
        pair = results.setdefault(paper_id, {})
        if branch in pair:
            raise ValueError('Duplicate assessment')
        pair[branch] = result
        audit.append({**item, 'response_sha256': digest(json.dumps(envelope, ensure_ascii=False, sort_keys=True))})
    if any(set(pair) != {'signature', 'review'} for pair in results.values()):
        raise ValueError('Incomplete assessment pairs')
    output.parent.mkdir(parents=True, exist_ok=True)
    # Do not overwrite a prior result or write a partial set on validation failure.
    with output.open('x', encoding='utf-8') as handle:
        for paper_id, pair in results.items():
            handle.write(json.dumps({'paper_id': paper_id, **pair,
                                    'model': execution_label,
                                    'execution': {'backend': 'isolated_agents',
                                                  'api_usage': None,
                                                  'note': 'Host-agent execution; token counts and hard output caps are not supplied by this collector.'}}, ensure_ascii=False) + '\n')
    output.with_suffix('.audit.json').write_text(json.dumps(audit, indent=2) + '\n', encoding='utf-8')
    print(f'Collected {len(results)} pairs into {output}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--manifest', required=True)
    p.add_argument('--requests', required=True)
    p.add_argument('--limit', type=int, default=5)
    p = sub.add_parser('collect')
    p.add_argument('--requests', required=True)
    p.add_argument('--responses', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--execution-label', required=True, help='Truthful host/model label; do not claim the API default was used')
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare(args.manifest, args.requests, args.limit)
    else:
        collect(args.requests, args.responses, args.output, args.execution_label)


if __name__ == '__main__':
    main()
