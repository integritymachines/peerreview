import unittest
from atlas import Interval,relation,randomized_additive,confounded_twins,benefit_bounds,simultaneous_feedback

class ReferenceCases(unittest.TestCase):
    def test_informative_congruence(self):
        r=randomized_additive()
        self.assertEqual((r["po"],r["scm"],r["se"]),(1.25,1.25,1.25))
    def test_observational_equivalence(self):
        r=confounded_twins()
        self.assertEqual(r["compatible_ate_examples"],[0,1])
        self.assertEqual(r["observational_joint"],[[.5,0.0],[0.0,.5]])
    def test_benefit_bounds(self):
        r=benefit_bounds()
        self.assertAlmostEqual(r["ate"],.4)
        self.assertAlmostEqual(r["benefit_without_crossworld_assumption"]["lower"],.4)
        self.assertAlmostEqual(r["benefit_without_crossworld_assumption"]["upper"],.7)
        self.assertAlmostEqual(r["benefit_with_monotonicity"],.4)
    def test_policy_vs_surgery(self):
        r=simultaneous_feedback()
        self.assertAlmostEqual(r["effect_of_policy_intercept_shift"],.625)
        self.assertAlmostEqual(r["effect_of_do_X"],.5)
    def test_set_relations(self):
        self.assertEqual(relation(Interval(1,2),Interval(1,2)),"congruent")
        self.assertEqual(relation(Interval(1.3,1.7),Interval(1,2)),"a-refines-b")
        self.assertEqual(relation(Interval(1,2),Interval(1.3,1.7)),"b-refines-a")
        self.assertEqual(relation(Interval(1,2),Interval(3,4)),"incompatible")
        self.assertEqual(relation(Interval(0,2),Interval(1,3)),"compatible-divergence")
    def test_singular_equilibrium(self):
        with self.assertRaises(ValueError):
            simultaneous_feedback(a=2,b=.5)

if __name__=="__main__":
    unittest.main()
