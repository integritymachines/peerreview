"""Render the frozen v2 comparison table and repeat statistics, without inference."""
import argparse
import json
from pathlib import Path

LABELS = {
    'q01': 'LaLonde (1986)', 'q02': 'Angrist–Krueger (1991)',
    'q03': 'Card–Krueger (1994)', 'q04': 'Rust (1987)',
    'q05': 'Berry–Levinsohn–Pakes (1995)', 'q06': 'Chetty (2008)',
    'q07': 'Hernán–Brumback–Robins (2000)', 'q08': 'Sachs et al. (2005)',
    'q09': 'Voight et al. (2012)', 'q10': 'Dell–Jones–Olken (2012)',
    'q11': 'Flaxman et al. (2020)', 'q12': 'Miguel–Kremer (2004)',
}
SHORT = {'potential_outcomes': 'PO', 'structural_causal_model': 'SCM',
         'structural_econometrics': 'SE', 'mechanistic_dynamical': 'MD', 'other': 'Other'}


def frameworks(values):
    return ', '.join(SHORT[x] for x in values) or 'Indeterminate'


def render(rows):
    out = ['| Paper | R/F/D | MDCI A | Blind B | Actually used C | Agreement |',
           '|---|---|---|---|---|---|']
    for row in rows:
        a, b, c = row['A'], row['B'], row['C']
        sig = '/'.join(f"{a['signature'][k]:.2f}" for k in ('R', 'F', 'D'))
        same = set(a['suitable_frameworks']) == set(b['suitable_frameworks'])
        agreement = 'Same component sets' if same else 'Partial component sets'
        if c['classification'] == 'underidentified':
            agreement += '; C indeterminate'
        elif set(c['actual_frameworks']) <= set(a['suitable_frameworks']) & set(b['suitable_frameworks']):
            agreement += '; used framework admissible'
        else:
            agreement += '; unresolved coverage gap'
        out.append(f"| {LABELS.get(row['paper_id'], row['paper_id'])} | {sig} | {frameworks(a['suitable_frameworks'])} | {frameworks(b['suitable_frameworks'])} | {frameworks(c['actual_frameworks'])} | {agreement} |")
    return '\n'.join(out) + '\n'


def repeat_metrics(rows):
    repeated = [r for r in rows if 'A_repeat' in r]
    per_case = []
    for r in repeated:
        first, second = r['A'], r['A_repeat']
        ds = {k: abs(first['signature'][k] - second['signature'][k]) for k in ('R', 'F', 'D')}
        a, b = set(first['suitable_frameworks']), set(second['suitable_frameworks'])
        per_case.append({'paper_id': r['paper_id'], 'first': first['signature'], 'repeat': second['signature'],
                         'absolute_differences': ds, 'candidate_sets_equal': a == b,
                         'candidate_jaccard': len(a & b) / len(a | b) if a | b else None,
                         'preference_stable': first['preference'] == second['preference'] and
                          set(first['preferred_frameworks']) == set(second['preferred_frameworks'])})
    n = len(per_case)
    return {'cases': per_case, 'summary': {
        'count': n, 'exact_signature_vectors': sum(not any(r['absolute_differences'].values()) for r in per_case),
        'coordinate_MAE': {k: sum(r['absolute_differences'][k] for r in per_case) / n if n else None for k in ('R', 'F', 'D')},
        'overall_coordinate_MAE': sum(sum(r['absolute_differences'].values()) for r in per_case) / (3*n) if n else None,
        'max_coordinate_difference': max((max(r['absolute_differences'].values()) for r in per_case), default=None),
        'exact_candidate_sets': sum(r['candidate_sets_equal'] for r in per_case)}}


def hybrid_metrics(rows):
    """Secondary structural audit; component equality alone is not full agreement."""
    def combinations(value):
        return {tuple(sorted(h['components'])) for h in value['hybrids']}
    output = {}
    for left in ('A', 'baseline'):
        cases = []
        for row in rows:
            l, r = row[left], row['B']
            same_components = set(l['suitable_frameworks']) == set(r['suitable_frameworks'])
            same_hybrids = combinations(l) == combinations(r)
            same_preference = (l['preference'] == r['preference'] and
                               set(l['preferred_frameworks']) == set(r['preferred_frameworks']))
            cases.append({'paper_id': row['paper_id'], 'component_sets_equal': same_components,
                          'hybrid_sets_equal': same_hybrids,
                          'full_recommendation_equal': same_components and same_hybrids and same_preference})
        output[left + '_B'] = {'cases': cases,
            'hybrid_sets_equal': sum(c['hybrid_sets_equal'] for c in cases),
            'full_recommendation_equal': sum(c['full_recommendation_equal'] for c in cases)}
    output['note'] = 'Secondary descriptive audit of explicit hybrid listings; omission is not a demonstrated rejection of compatibility.'
    return output


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--records', required=True)
    p.add_argument('--table', required=True)
    p.add_argument('--repeats', required=True)
    a = p.parse_args()
    rows = [json.loads(s) for s in Path(a.records).read_text().splitlines() if s.strip()]
    for path, value in [(a.table, render(rows)), (a.repeats, json.dumps(repeat_metrics(rows), indent=2) + '\n')]:
        with Path(path).open('x', encoding='utf-8') as f:
            f.write(value)


if __name__ == '__main__':
    main()
