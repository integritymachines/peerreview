"""Frozen, file-based MDCI v2 requests. Runs no inference.

The host must seal completed A/B/baseline runs before launching C workers.
The seal is an audit protocol, not a filesystem security boundary.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

FRAMEWORKS = frozenset(('potential_outcomes', 'structural_causal_model',
                        'structural_econometrics', 'mechanistic_dynamical', 'other'))
BRANCHES = ('A', 'B', 'C', 'baseline')
PROMPTS = Path(__file__).parent / 'v2' / 'prompts'


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def write_new(path, data):
    path = Path(path)
    with path.open('xb') as stream:
        stream.write(data)


def ids(value, label, minimum=0):
    require(isinstance(value, list), label + ' must be a list')
    require(all(isinstance(v, str) and v in FRAMEWORKS for v in value),
            label + ': unknown framework (identification designs are not frameworks)')
    require(len(value) == len(set(value)) and len(value) >= minimum, label + ': invalid components')
    return set(value)


def validate(result, branch):
    require(isinstance(result, dict), 'result must be an object')
    if branch == 'C':
        require({'actual_frameworks', 'classification', 'identification_designs', 'hybrid_components',
                 'formal_evidence', 'limitations'} <= result.keys(), 'missing C result fields')
        actual = ids(result.get('actual_frameworks'), 'actual_frameworks')
        classification = result.get('classification')
        require(classification in ('explicit', 'apparatus_supported', 'hybrid', 'underidentified'), 'invalid classification')
        require(actual or classification == 'underidentified', 'C needs frameworks or underidentified')
        hybrid = ids(result.get('hybrid_components'), 'hybrid_components')
        require(not hybrid or hybrid <= actual, 'hybrid components must be actual frameworks')
        require(classification != 'hybrid' or len(hybrid) >= 2, 'hybrid needs multiple components')
        for name in ('identification_designs', 'formal_evidence', 'limitations'):
            require(isinstance(result.get(name), list), name + ' must be a list')
        require(all(isinstance(x, str) for x in result['identification_designs']), 'designs must be strings')
        for evidence in result['formal_evidence']:
            require(isinstance(evidence, dict) and all(isinstance(evidence.get(k), str)
                    for k in ('location', 'quote', 'paraphrase', 'equation_description')), 'invalid formal evidence')
        require(len(result['formal_evidence']) >= 2, 'C requires at least two formal evidence records')
        require(sum(len(e['quote'].split()) for e in result['formal_evidence']) <= 20,
                'C source quotes exceed 20 words total')
        return
    require({'suitable_frameworks', 'preferred_frameworks', 'preference', 'framework_assessments',
             'hybrids', 'material_advantage', 'evidence', 'limitations'} <= result.keys(), 'missing result fields')
    suitable = ids(result.get('suitable_frameworks'), 'suitable_frameworks')
    preferred = ids(result.get('preferred_frameworks'), 'preferred_frameworks')
    require(preferred <= suitable, 'preferred must be a subset of suitable')
    preference = result.get('preference')
    require(preference in ('discriminating', 'equally_admissible', 'indeterminate'), 'invalid preference')
    for name in ('framework_assessments', 'hybrids', 'evidence', 'limitations'):
        require(isinstance(result.get(name), list), name + ' must be a list')
    require(all(isinstance(x, dict) for x in result['framework_assessments']), 'assessments must be objects')
    for assessment in result['framework_assessments']:
        # Assessment objects may carry explanations, but any framework identity is locked.
        if 'framework' in assessment:
            ids([assessment['framework']], 'assessment framework')
        if 'framework_id' in assessment:
            ids([assessment['framework_id']], 'assessment framework')
    for hybrid in result['hybrids']:
        require(isinstance(hybrid, dict), 'hybrid must be an object')
        require(ids(hybrid.get('components'), 'hybrid components', 2) <= suitable,
                'hybrid components must be suitable')
    advantage = result.get('material_advantage')
    require(advantage is None or isinstance(advantage, str), 'invalid material_advantage')
    if preference == 'discriminating':
        require(preferred and advantage and advantage.strip() and result['evidence'],
                'discriminating preference needs preferred frameworks, explanation and evidence')
    if branch in ('A', 'A_repeat'):
        signature = result.get('signature')
        require(isinstance(signature, dict) and set(signature) == {'R', 'F', 'D'}, 'invalid signature')
        require(all(type(v) in (float, int) and 0 <= v <= 1 for v in signature.values()), 'signature out of bounds')
        require(all(v * 4 == int(v * 4) for v in signature.values()), 'signature requires quarter steps')
        for name in ('coordinate_evidence', 'admissible_priors', 'unresolved_orientations'):
            require(isinstance(result.get(name), list), name + ' must be a list')


def prepare(manifest, requests, limit=12, repeat_ids=(), prompts=None):
    require(type(limit) is int and 1 <= limit <= 12, 'limit must be 1..12')
    manifest = Path(manifest).resolve()
    selected = rows(manifest)[:limit]
    require(selected, 'empty manifest')
    paper_ids = [r['paper_id'] for r in selected]
    require(all(isinstance(p, str) and re.fullmatch(r'[A-Za-z0-9_-]+', p) for p in paper_ids) and len(set(paper_ids)) == len(paper_ids), 'invalid paper IDs')
    require(len(set(repeat_ids)) == len(repeat_ids) and set(repeat_ids) <= set(paper_ids), 'repeat IDs must be unique selected papers')
    prompts = Path(prompts or PROMPTS)
    inputs = {}

    def frozen(path):
        path = Path(path).resolve()
        data = path.read_bytes()
        inputs[str(path)] = digest(data)
        return data

    frozen(manifest)
    instructions = {b: frozen(prompts / (b + '.txt')).decode('utf-8') for b in BRANCHES}
    output = []
    for row in selected:
        dossier_path = (manifest.parent / row['dossier']).resolve()
        paper_path = (manifest.parent / row['paper']).resolve()
        dossier = frozen(dossier_path).decode('utf-8')
        require(100 <= len(dossier) <= 12000, 'dossier must contain 100..12000 characters; no truncation allowed')
        frozen(paper_path)
        c_assets = {}
        if row.get('pdf') is not None:
            pdf_path = (manifest.parent / row['pdf']).resolve()
            c_assets.update(pdf_path=str(pdf_path), pdf_sha256=digest(frozen(pdf_path)))
        if 'supplements' in row:
            require(isinstance(row['supplements'], list) and all(isinstance(p, str) for p in row['supplements']),
                    'supplements must be a list of paths')
            supplemental_paths = [(manifest.parent / p).resolve() for p in row['supplements']]
            c_assets.update(supplemental_source_paths=[str(p) for p in supplemental_paths],
                            supplemental_source_hashes=[digest(frozen(p)) for p in supplemental_paths])
        baseline = canonical({k: row[k] for k in ('domain', 'estimand')}).decode('utf-8')
        for branch in (*BRANCHES, *(('A_repeat',) if row['paper_id'] in repeat_ids else ())):
            prompt = instructions['A' if branch == 'A_repeat' else branch]
            item = {'paper_id': row['paper_id'], 'branch': branch, 'instructions': prompt,
                    'prompt_sha256': digest(prompt.encode())}
            if branch == 'C':
                item.update(source_path=str(paper_path), source_sha256=inputs[str(paper_path)], **c_assets)
            else:
                source = baseline if branch == 'baseline' else dossier
                item.update(source=source, source_sha256=digest(source.encode()))
            item['request_hash'] = digest(canonical(item))
            output.append(item)
    payload = b''.join(canonical(r) + b'\n' for r in output)
    index = {'version': 2, 'inputs': inputs, 'requests_sha256': digest(payload),
             'paper_ids': paper_ids, 'repeat_ids': list(repeat_ids)}
    index['index_hash'] = digest(canonical(index))
    target = Path(requests)
    require(not target.exists(), 'request directory already exists; refusing overwrite')
    target.mkdir(parents=True)
    write_new(target / 'requests.jsonl', payload)
    write_new(target / 'index.json', canonical(index))
    return output


def verify(requests):
    root = Path(requests)
    index = read_json(root / 'index.json')
    claimed = index.pop('index_hash')
    require(claimed == digest(canonical(index)), 'index changed')
    index['index_hash'] = claimed
    require(digest((root / 'requests.jsonl').read_bytes()) == index['requests_sha256'], 'requests changed')
    for path, expected in index['inputs'].items():
        require(digest(Path(path).read_bytes()) == expected, 'frozen input changed: ' + path)
    request_rows = rows(root / 'requests.jsonl')
    for row in request_rows:
        check = dict(row)
        claimed_hash = check.pop('request_hash')
        require(digest(canonical(check)) == claimed_hash, 'request hash changed')
    return index, {(r['paper_id'], r['branch']): r for r in request_rows}


def responses_from(directory, requested):
    responses, files = {}, {}
    for path in sorted(Path(directory).glob('*.json')):
        envelope = read_json(path)
        key = (envelope.get('paper_id'), envelope.get('branch'))
        require(key in requested and key not in responses, 'unexpected or duplicate response identity')
        require(envelope.get('request_hash') == requested[key]['request_hash'], 'response request identity mismatch')
        validate(envelope.get('result'), key[1])
        responses[key] = envelope['result']
        files[key] = path.resolve()
    return responses, files


def seal(requests, responses):
    index, requested = verify(requests)
    result, files = responses_from(responses, requested)
    require(not any(k[1] == 'C' for k in result), 'C response exists before A/B seal')
    required = {k for k in requested if k[1] != 'C'}
    require(set(result) == required, 'all A/B/baseline/repeat responses required before sealing')
    sealed = {'index_hash': index['index_hash'], 'responses': {
        str(files[k]): digest(files[k].read_bytes()) for k in sorted(required)}}
    write_new(Path(requests) / 'AB_SEALED.json', canonical(sealed))


def collect(requests, responses, output):
    index, requested = verify(requests)
    seal_path = Path(requests) / 'AB_SEALED.json'
    require(seal_path.exists(), 'seal A/B responses before launching or collecting C')
    sealed = read_json(seal_path)
    require(sealed['index_hash'] == index['index_hash'], 'seal index mismatch')
    for name, expected in sealed['responses'].items():
        require(digest(Path(name).read_bytes()) == expected, 'sealed response changed')
    result, files = responses_from(responses, requested)
    require(set(result) == set(requested), 'incomplete responses; nothing written')
    ab_paths = {str(files[k]) for k in files if k[1] != 'C'}
    require(ab_paths == set(sealed['responses']), 'sealed response paths changed')
    require(all(files[k].stat().st_mtime_ns >= seal_path.stat().st_mtime_ns for k in files if k[1] == 'C'),
            'C response predates seal')
    grouped = [{'paper_id': pid, **{b: result[(pid, b)] for p, b in requested if p == pid},
                'execution': {'model_label': 'unknown', 'usage': 'unknown'}} for pid in index['paper_ids']]
    write_new(output, b''.join(canonical(r) + b'\n' for r in grouped))
    return grouped


def set_metrics(left, right):
    left, right = set(left), set(right)
    union = left | right
    return {'equal': left == right, 'intersection_size': len(left & right),
            'jaccard': len(left & right) / len(union) if union else None,
            'left_size': len(left), 'right_size': len(right)}


def compare(records):
    details = []
    for row in records:
        for branch in (*BRANCHES, *(('A_repeat',) if 'A_repeat' in row else ())):
            validate(row[branch], branch)
        detail = {'paper_id': row['paper_id']}
        for name, l, r in (('A_B', 'A', 'B'), ('baseline_B', 'baseline', 'B')):
            left, right = row[l], row[r]
            detail[name] = set_metrics(left['suitable_frameworks'], right['suitable_frameworks'])
            detail[name].update(preferred_agreement=set(left['preferred_frameworks']) == set(right['preferred_frameworks']),
                                left_abstention=left['preference'] == 'indeterminate',
                                right_abstention=right['preference'] == 'indeterminate')
        a, base = detail['A_B']['jaccard'], detail['baseline_B']['jaccard']
        detail['paired_jaccard_difference'] = a - base if a is not None and base is not None else None
        c = row['C']
        unknown = c['classification'] == 'underidentified'
        detail['C_underidentified'] = unknown
        detail['admissibility_coverage'] = {b: None if unknown or not c['actual_frameworks'] else
            set(c['actual_frameworks']) <= set(row[b]['suitable_frameworks']) for b in ('A', 'B')}
        if 'A_repeat' in row:
            differences = {k: abs(row['A']['signature'][k] - row['A_repeat']['signature'][k]) for k in ('R', 'F', 'D')}
            detail['repeat'] = {'coordinate_absolute_differences': differences,
                'mean_absolute_difference': sum(differences.values()) / 3, 'max_absolute_difference': max(differences.values()),
                'framework_sets': set_metrics(row['A']['suitable_frameworks'], row['A_repeat']['suitable_frameworks']),
                'preference_stable': row['A']['preference'] == row['A_repeat']['preference'] and
                    set(row['A']['preferred_frameworks']) == set(row['A_repeat']['preferred_frameworks'])}
        details.append(detail)
    summary = {'paper_count': len(details), 'C_underidentified_count': sum(d['C_underidentified'] for d in details)}
    for pair in ('A_B', 'baseline_B'):
        values = [d[pair] for d in details]
        js = [v['jaccard'] for v in values if v['jaccard'] is not None]
        summary[pair] = {'count': len(values), 'equal_count': sum(v['equal'] for v in values),
                         'preferred_agreement_count': sum(v['preferred_agreement'] for v in values),
                         'jaccard_denominator': len(js), 'mean_jaccard': sum(js) / len(js) if js else None,
                         'left_abstention_count': sum(v['left_abstention'] for v in values),
                         'right_abstention_count': sum(v['right_abstention'] for v in values)}
    paired = [d['paired_jaccard_difference'] for d in details if d['paired_jaccard_difference'] is not None]
    summary['admissibility_coverage'] = {b: {
        'covered_count': sum(d['admissibility_coverage'][b] is True for d in details),
        'denominator': sum(d['admissibility_coverage'][b] is not None for d in details)} for b in ('A', 'B')}
    summary['paired_jaccard_difference'] = {'denominator': len(paired), 'mean': sum(paired) / len(paired) if paired else None}
    return {'summary': summary, 'papers': details, 'interpretation': 'Coverage measures admissibility only; no causal fit or mismatch is inferred.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('prepare')
    p.add_argument('--manifest', required=True)
    p.add_argument('--requests', required=True)
    p.add_argument('--limit', type=int, default=12)
    p.add_argument('--repeat-ids', nargs='*', default=[])
    for command in ('seal', 'collect'):
        p = sub.add_parser(command)
        p.add_argument('--requests', required=True)
        p.add_argument('--responses', required=True)
        if command == 'collect':
            p.add_argument('--output', required=True)
    p = sub.add_parser('compare')
    p.add_argument('--records', required=True)
    p.add_argument('--output', required=True)
    args = vars(parser.parse_args())
    command = args.pop('command')
    try:
        if command == 'compare':
            write_new(args['output'], canonical(compare(rows(args['records']))) + b'\n')
        else:
            globals()[command](**args)
    except (ValueError, KeyError, OSError, TypeError) as error:
        parser.exit(2, str(error) + '\n')


if __name__ == '__main__':
    main()
