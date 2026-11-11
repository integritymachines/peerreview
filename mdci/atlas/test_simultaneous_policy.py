import json
from pathlib import Path
import unittest
from fractions import Fraction as F
from simultaneous_policy import (Model, SHOCKS, po_response, iterate, calibrate,
                                observational_twin, average_y, serialized_results)

class SimultaneousPolicy(unittest.TestCase):
    def test_exact_equilibria_and_equation_residuals(self):
        m = Model()
        self.assertEqual(m.equilibrium(), (F(9,4), F(25,8)))
        self.assertEqual(m.equilibrium(lam=F(1), k=F(1,5)), (F(32,7), F(30,7)))
        for a in (F(-2), F(0), F(2,5), F(3)):
            for k in (F(0), F(1,5)):
                candidate = Model(a=a)
                for u,v in SHOCKS:
                    xy = candidate.equilibrium(u,v,F(1),k)
                    self.assertEqual(candidate.residuals(*xy,F(1),k), (u,v))
                    self.assertEqual(xy, po_response(candidate,u,v,F(1),k))

    def test_policy_effects_and_nonadditivity(self):
        m=Model()
        base=m.equilibrium()[1]
        intercept=m.equilibrium(lam=F(1))[1]-base
        slope=m.equilibrium(k=F(1,5))[1]-base
        both=m.equilibrium(lam=F(1),k=F(1,5))[1]-base
        self.assertEqual((intercept,slope,both), (F(5,8),F(25,56),F(65,56)))
        self.assertEqual(both-intercept-slope,F(5,56))
        self.assertEqual(m.clamp_x(F(1))[1]-m.clamp_x(F(0))[1],F(1,2))

    def test_distribution_and_individual_counterfactual(self):
        m=Model()
        ys=[m.equilibrium(u,v,F(1),F(1,5))[1] for u,v in SHOCKS]
        mean=sum(ys)/4
        self.assertEqual(mean,F(30,7))
        self.assertEqual(sum((y-mean)**2 for y in ys)/4,F(125,49))
        xy=m.equilibrium(F(1),F(-1))
        u,v=m.residuals(*xy)
        self.assertEqual(m.equilibrium(u,v,F(1),F(1,5))[1]-xy[1],F(15,14))

    def test_calibration_identifies_parameters(self):
        m=Model()
        mx,my=m.equilibrium()
        b=m.clamp_x(F(1))[1]-m.clamp_x(F(0))[1]
        r=m.equilibrium(lam=F(1))[1]-my
        self.assertEqual(calibrate(mx,my,b,r),m)
        with self.assertRaises(ValueError):
            calibrate(mx,my,F(0),r)

    def test_full_baseline_law_equal_policy_laws_differ(self):
        m=Model()
        twin,shocks=observational_twin(m,F(0))
        self.assertEqual([m.equilibrium(*s) for s in SHOCKS],
                         [twin.equilibrium(*s) for s in shocks])
        self.assertEqual(sum(s[0] for s in shocks),0)
        self.assertEqual(sum(s[1] for s in shocks),0)
        base=average_y(m,SHOCKS)
        self.assertEqual(average_y(twin,shocks,F(1),F(1,5))-base,F(65,72))
        self.assertNotEqual(average_y(m,SHOCKS,F(1),F(1,5)),
                            average_y(twin,shocks,F(1),F(1,5)))

    def test_reduced_form_preserves_policy_not_clamps(self):
        m=Model()
        # A reduced-form DAG has no X -> Y edge; clamping X leaves Y unchanged.
        reduced_form_y=po_response(m,F(1),F(-1))[1]
        self.assertNotEqual(reduced_form_y,m.clamp_x(F(0),F(-1))[1])
        self.assertEqual(po_response(m,F(1),F(-1),F(1),F(1,5)),
                         m.equilibrium(F(1),F(-1),F(1),F(1,5)))

    def test_stable_adjustment_converges(self):
        m=Model()
        for u,v in SHOCKS:
            for got,want in zip(iterate(m,u,v,F(1),F(1,5)),
                                m.equilibrium(u,v,F(1),F(1,5))):
                self.assertAlmostEqual(got,float(want),places=12)

    def test_unique_does_not_imply_dynamic_stability(self):
        m=Model(a=F(3))
        exact=m.equilibrium()
        self.assertEqual(m.residuals(*exact),(0,0))
        self.assertGreater(abs(iterate(m,F(0),F(0),F(0),F(0),80)[0]-float(exact[0])),1000)

    def test_singularity_none_and_multiple(self):
        m=Model(a=F(2))
        with self.assertRaises(ValueError):
            m.equilibrium()  # X=1+2(2+.5X) implies 0=5: no solution.
        multiple=Model(a=F(2),c=F(0),d=F(0))
        with self.assertRaises(ValueError):
            multiple.equilibrium()
        for x in (F(-2),F(0),F(5)):
            self.assertEqual(multiple.residuals(x,x/2),(0,0))
        # A nonsingular baseline can become singular after a policy change.
        with self.assertRaises(ValueError):
            Model().equilibrium(k=F(8,5))
        self.assertEqual(m.clamp_x(F(0)),(0,2))

    def test_saved_results_reproduce(self):
        path=Path(__file__).with_name('RESULTS_v02.json')
        self.assertEqual(json.loads(path.read_text(encoding='utf-8')),json.loads(serialized_results()))

    def test_unrestricted_target_regime_can_have_any_mean(self):
        m=Model()
        base=m.equilibrium()[1]
        effect=F(65,56)
        for desired in (F(-100),F(0),F(1,7),F(100)):
            eta=F(7,10)*(desired-effect)
            # This changed d is used ONLY at k=1/5. All k=0 arms use m.
            target_model=Model(d=m.d+eta)
            actual=target_model.equilibrium(lam=F(1),k=F(1,5))[1]-base
            self.assertEqual(actual,desired)

if __name__ == '__main__':
    unittest.main()
