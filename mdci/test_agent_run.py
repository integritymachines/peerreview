"""Offline checks for branch separation, input freezing and safe collection."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from mdci import agent_run, run


class AgentRunTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = self.root / 'manifest.jsonl'
        self.paper = 'PAPER-ONLY treatment estimate and chosen method. ' * 5
        self.dossier = 'DOSSIER-ONLY ex-ante system and observation structure. ' * 5
        (self.root / 'paper.txt').write_text(self.paper)
        (self.root / 'dossier.txt').write_text(self.dossier)
        self.manifest.write_text(json.dumps({'paper_id': 'p001', 'paper': 'paper.txt', 'dossier': 'dossier.txt'}) + '\n')
        self.requests = self.root / 'requests'
        with contextlib.redirect_stdout(io.StringIO()):
            agent_run.prepare(self.manifest, self.requests)
        self.responses = self.root / 'responses'
        self.output = self.root / 'results.jsonl'

    def write_responses(self):
        results = {
            'signature': {'signature': {'R': 0.5, 'F': 0.3, 'D': 0.2}, 'recommended_frameworks': []},
            'review': {'framework_used': ['adjustment'], 'preferred_frameworks': [], 'fit': 'indeterminate', 'materially_better_alternative': False},
        }
        for branch, result in results.items():
            request = json.loads((self.requests / branch / 'p001.json').read_text())
            envelope = {k: request[k] for k in ('paper_id', 'branch', 'request_hash')}
            envelope['result'] = result
            path = self.responses / branch / 'p001.json'
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps(envelope))

    def collect(self):
        with contextlib.redirect_stdout(io.StringIO()):
            agent_run.collect(self.requests, self.responses, self.output, 'test host')

    def test_requests_do_not_cross_branch_inputs(self):
        signature = json.loads((self.requests / 'signature/p001.json').read_text())
        review = json.loads((self.requests / 'review/p001.json').read_text())
        self.assertEqual(signature['source'], self.dossier)
        self.assertEqual(review['source'], self.paper)
        self.assertNotIn('PAPER-ONLY', json.dumps(signature))
        self.assertNotIn('DOSSIER-ONLY', json.dumps(review))
        self.assertEqual(review['instructions'], (run.ROOT / 'review-lite.txt').read_text())
        self.assertEqual(signature['instructions'], (run.ROOT / 'signature-lite.txt').read_text())

    def test_collect_preserves_abstention_and_records_backend(self):
        self.write_responses()
        self.collect()
        row = run.read_jsonl(self.output)[0]
        self.assertEqual(row['model'], 'test host')
        self.assertIsNone(row['execution']['api_usage'])
        self.assertIsNone(run.compare([row])['binary_agreement'])
        self.assertEqual(len(json.loads(self.output.with_suffix('.audit.json').read_text())), 2)
        with self.assertRaises(FileExistsError):
            self.collect()

    def test_reject_changed_request_before_output(self):
        self.write_responses()
        path = self.requests / 'signature/p001.json'
        request = json.loads(path.read_text())
        request['source'] += ' changed'
        path.chmod(0o600)
        path.write_text(json.dumps(request))
        with self.assertRaisesRegex(ValueError, 'Changed request'):
            self.collect()
        self.assertFalse(self.output.exists())

    def test_reject_response_from_wrong_branch(self):
        self.write_responses()
        path = self.responses / 'review/p001.json'
        envelope = json.loads(path.read_text())
        envelope['branch'] = 'signature'
        path.write_text(json.dumps(envelope))
        with self.assertRaisesRegex(ValueError, 'Response identity mismatch'):
            self.collect()
        self.assertFalse(self.output.exists())

    def test_missing_response_does_not_write_partial_results(self):
        self.write_responses()
        (self.responses / 'review/p001.json').unlink()
        with self.assertRaises(FileNotFoundError):
            self.collect()
        self.assertFalse(self.output.exists())

    def test_source_limits_and_existing_run_are_not_bypassed(self):
        with self.assertRaises(FileExistsError):
            agent_run.prepare(self.manifest, self.requests)
        (self.root / 'paper.txt').write_text('x' * 25001)
        with self.assertRaisesRegex(ValueError, 'source exceeds'):
            agent_run.prepare(self.manifest, self.root / 'too-long')
        self.assertTrue((self.root / 'too-long/PREPARATION_FAILED').exists())
        with self.assertRaisesRegex(ValueError, 'Hard pilot limit'):
            agent_run.prepare(self.manifest, self.root / 'too-many', 6)


if __name__ == '__main__':
    unittest.main()
