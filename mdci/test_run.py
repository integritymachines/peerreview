"""Offline, deterministic tests; no API key or model use."""
import unittest
from mdci import run

class PilotTests(unittest.TestCase):
    def test_signature_range(self):
        obj={"signature":{"R":0.8,"F":0.2,"D":1.0},"recommended_frameworks":["randomized"]}
        self.assertEqual(run.validate("signature",obj)["signature"]["D"],1)
        with self.assertRaises(ValueError):
            run.validate("signature",{"signature":{"R":0.8,"F":1.1,"D":0},"recommended_frameworks":[]})
    def test_match_and_mismatch(self):
        rows=[
          {"paper_id":"a","signature":{"signature":{"R":0.8,"F":0.2,"D":1},"recommended_frameworks":["randomized"]},
           "review":{"framework_used":["randomized"],"preferred_frameworks":["randomized"],"fit":"appropriate","materially_better_alternative":False}},
          {"paper_id":"b","signature":{"signature":{"R":0.5,"F":0.9,"D":0.2},"recommended_frameworks":["adjustment"]},
           "review":{"framework_used":["instrumental_variables"],"preferred_frameworks":["adjustment"],"fit":"mismatch","reason":"Unsupported instrument","materially_better_alternative":True}}]
        result=run.compare(rows)
        self.assertEqual(result["review_appropriate"],1)
        self.assertEqual(result["review_mismatch"],1)
        self.assertEqual(result["binary_agreement"],1.0)
    def test_empty_review_is_not_a_forced_mismatch(self):
        rows=[{"paper_id":"x","signature":{"signature":{"R":0.5,"F":0.5,"D":0.5},"recommended_frameworks":[]},
               "review":{"framework_used":["other"],"preferred_frameworks":[],"fit":"indeterminate","materially_better_alternative":False}}]
        self.assertIsNone(run.compare(rows)["binary_agreement"])

if __name__=="__main__":
    unittest.main()
