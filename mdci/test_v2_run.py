import json
from pathlib import Path
import tempfile
import unittest

from mdci import v2_run as run

PO = 'potential_outcomes'
SCM = 'structural_causal_model'


def result(branch):
    if branch == 'C':
        return dict(actual_frameworks=[PO], classification='apparatus_supported', identification_designs=['DiD'],
                    hybrid_components=[], formal_evidence=[dict(location='p. 1', quote='brief source quote',
                    paraphrase='Explanation', equation_description='Equation description') for _ in range(2)], limitations=[])
    value = dict(suitable_frameworks=[PO, SCM], preferred_frameworks=[], preference='equally_admissible',
                 framework_assessments=[], hybrids=[{'components': [PO, SCM]}], material_advantage=None,
                 evidence=[], limitations=[])
    if branch in ('A', 'A_repeat'):
        value.update(signature=dict(R=.25, F=.5, D=.75), coordinate_evidence=[], admissible_priors=[], unresolved_orientations=[])
    return value


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.prompts = self.root / 'prompts'
        self.prompts.mkdir()
        for branch in run.BRANCHES:
            (self.prompts / (branch + '.txt')).write_text('instructions ' + branch)
        (self.root / 'dossier.txt').write_text('Distinctive dossier content. ' * 5)
        (self.root / 'paper.txt').write_text('Complete paper content')
        (self.root / 'paper.pdf').write_bytes(b'%PDF-1.4 fixture')
        (self.root / 'supplement.txt').write_text('Supplement fixture')
        self.manifest = self.root / 'manifest.jsonl'
        self.manifest.write_text(json.dumps(dict(paper_id='q02', dossier='dossier.txt', paper='paper.txt',
                                                domain='economics', estimand='effect', pdf='paper.pdf',
                                                supplements=['supplement.txt'])) + '\n')
        self.requests = self.root / 'requests'
        self.responses = self.root / 'responses'
        self.responses.mkdir()

    def prepare(self, **kwargs):
        self.items = run.prepare(self.manifest, self.requests, prompts=self.prompts, **kwargs)
        return {r['branch']: r for r in self.items}

    def respond(self, branches):
        for item in self.items:
            if item['branch'] in branches:
                envelope = {k: item[k] for k in ('paper_id', 'branch', 'request_hash')}
                envelope['result'] = result(item['branch'])
                (self.responses / (item['branch'] + '.json')).write_text(json.dumps(envelope))

    def test_input_isolation_and_repeat(self):
        req = self.prepare(repeat_ids=['q02'])
        self.assertEqual(req['A']['source'], req['B']['source'])
        self.assertEqual(req['A']['source_sha256'], req['B']['source_sha256'])
        self.assertEqual(json.loads(req['baseline']['source']), {'domain': 'economics', 'estimand': 'effect'})
        self.assertNotIn('source', req['C'])
        self.assertEqual(req['C']['source_path'], str(self.root / 'paper.txt'))
        self.assertEqual(req['A']['instructions'], req['A_repeat']['instructions'])
        self.assertEqual(req['A']['source'], req['A_repeat']['source'])
        self.assertEqual(req['C']['pdf_path'], str(self.root / 'paper.pdf'))
        self.assertEqual(req['C']['supplemental_source_paths'], [str(self.root / 'supplement.txt')])
        index = json.loads((self.requests / 'index.json').read_text())
        for filename in ('paper.pdf', 'supplement.txt'):
            self.assertIn(str(self.root / filename), index['inputs'])
        for branch in ('A', 'B', 'baseline', 'A_repeat'):
            self.assertNotIn('pdf_path', req[branch])
            self.assertNotIn('supplemental_source_paths', req[branch])
        (self.root / 'paper.pdf').write_bytes(b'changed PDF')
        with self.assertRaisesRegex(ValueError, 'input changed'):
            run.verify(self.requests)
        with self.assertRaises(ValueError):
            run.prepare(self.manifest, self.requests, prompts=self.prompts)

    def test_round_trip_and_incomplete_no_write(self):
        self.prepare(repeat_ids=['q02'])
        self.respond(['A', 'B', 'baseline', 'A_repeat'])
        run.seal(self.requests, self.responses)
        output = self.root / 'records.jsonl'
        with self.assertRaises(ValueError):
            run.collect(self.requests, self.responses, output)
        self.assertFalse(output.exists())
        self.respond(['C'])
        collected = run.collect(self.requests, self.responses, output)
        comparison = run.compare(collected)
        self.assertEqual(comparison['summary']['A_B']['mean_jaccard'], 1)
        self.assertEqual(comparison['papers'][0]['repeat']['max_absolute_difference'], 0)
        self.assertEqual(collected[0]['execution']['usage'], 'unknown')

    def test_c_before_seal_refused(self):
        self.prepare()
        self.respond(run.BRANCHES)
        with self.assertRaisesRegex(ValueError, 'before A/B seal'):
            run.seal(self.requests, self.responses)
        with self.assertRaisesRegex(ValueError, 'seal A/B'):
            run.collect(self.requests, self.responses, self.root / 'out')

    def test_changed_inputs_and_outputs_rejected(self):
        self.prepare()
        self.respond(['A', 'B', 'baseline'])
        run.seal(self.requests, self.responses)
        self.respond(['C'])
        original = (self.root / 'paper.txt').read_text()
        (self.root / 'paper.txt').write_text(original + ' changed')
        with self.assertRaisesRegex(ValueError, 'input changed'):
            run.collect(self.requests, self.responses, self.root / 'out')
        (self.root / 'paper.txt').write_text(original)
        with (self.responses / 'A.json').open('a') as stream:
            stream.write(' ')
        with self.assertRaisesRegex(ValueError, 'response changed'):
            run.collect(self.requests, self.responses, self.root / 'out')
        self.assertFalse((self.root / 'out').exists())

    def test_identity_and_prompt_integrity(self):
        self.prepare()
        self.respond(['A', 'B', 'baseline'])
        path = self.responses / 'A.json'
        envelope = json.loads(path.read_text())
        envelope['request_hash'] = 'wrong'
        path.write_text(json.dumps(envelope))
        with self.assertRaisesRegex(ValueError, 'identity mismatch'):
            run.seal(self.requests, self.responses)
        (self.prompts / 'A.txt').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'input changed'):
            run.verify(self.requests)

    def test_framework_design_and_hybrid_validation(self):
        for label in ['IV', 'DiD', 'RD', 'hybrid']:
            value = result('B')
            value['suitable_frameworks'] = [label]
            with self.assertRaises(ValueError):
                run.validate(value, 'B')
        value = result('B')
        value['hybrids'] = [{'components': [PO]}]
        with self.assertRaises(ValueError):
            run.validate(value, 'B')
        value = result('C')
        value.update(classification='hybrid', hybrid_components=[PO])
        with self.assertRaises(ValueError):
            run.validate(value, 'C')
        value = result('B')
        value.update(preference='discriminating', preferred_frameworks=[PO])
        with self.assertRaises(ValueError):
            run.validate(value, 'B')

    def test_unknown_and_metric_denominators(self):
        self.assertIsNone(run.set_metrics([], [])['jaccard'])
        self.assertEqual(run.set_metrics([PO], [])['jaccard'], 0)
        self.assertEqual(run.set_metrics([PO, SCM], [PO])['jaccard'], .5)
        record = {'paper_id': 'x', **{b: result(b) for b in run.BRANCHES}}
        for b in ('A', 'B', 'baseline'):
            record[b]['suitable_frameworks'] = []
            record[b]['hybrids'] = []
        record['C'].update(classification='underidentified', actual_frameworks=[])
        report = run.compare([record])
        self.assertEqual(report['summary']['C_underidentified_count'], 1)
        self.assertEqual(report['summary']['A_B']['jaccard_denominator'], 0)
        self.assertIsNone(report['papers'][0]['admissibility_coverage']['A'])
        self.assertEqual(report['summary']['paired_jaccard_difference']['denominator'], 0)

    def test_c_evidence_bounds_and_prepare_guards(self):
        value = result('C')
        value['formal_evidence'].pop()
        with self.assertRaisesRegex(ValueError, 'at least two'):
            run.validate(value, 'C')
        value = result('C')
        value['formal_evidence'][0]['quote'] = 'word ' * 21
        with self.assertRaisesRegex(ValueError, '20 words'):
            run.validate(value, 'C')
        manifest = json.loads(self.manifest.read_text())
        manifest['paper_id'] = '../q02'
        self.manifest.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'invalid paper IDs'):
            self.prepare()
        manifest['paper_id'] = 'q02'
        self.manifest.write_text(json.dumps(manifest))
        (self.root / 'dossier.txt').write_text('Too short')
        with self.assertRaisesRegex(ValueError, '100..12000'):
            self.prepare()
        self.assertFalse(self.requests.exists())

    def test_repeat_selection_and_signature_bounds(self):
        for limit in (0, 13):
            with self.assertRaises(ValueError):
                self.prepare(limit=limit)
        with self.assertRaises(ValueError):
            self.prepare(repeat_ids=['q99'])
        with self.assertRaises(ValueError):
            self.prepare(repeat_ids=['q02', 'q02'])
        value = result('A_repeat')
        value['signature']['R'] = .3
        with self.assertRaisesRegex(ValueError, 'quarter steps'):
            run.validate(value, 'A_repeat')
        value['signature']['R'] = 1.01
        with self.assertRaises(ValueError):
            run.validate(value, 'A_repeat')


if __name__ == '__main__':
    unittest.main()
