"""Exact-rational reference study E; standard library, no external data."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json

@dataclass(frozen=True)
class Model:
    a: F = F(2, 5)
    b: F = F(1, 2)
    c: F = F(1)
    d: F = F(2)

    def equilibrium(self, u=F(0), v=F(0), lam=F(0), k=F(0)):
        det = 1 - (self.a + k) * self.b
        if det == 0:
            raise ValueError('No unique equilibrium: distinguish none from multiple')
        x = (self.c + lam + u + (self.a + k) * (self.d + v)) / det
        return x, self.d + self.b * x + v

    def clamp_x(self, x, v=F(0)):
        return x, self.d + self.b * x + v

    def residuals(self, x, y, lam=F(0), k=F(0)):
        return x - self.c - lam - (self.a + k) * y, y - self.d - self.b * x

def po_response(m, u, v, lam=F(0), k=F(0)):
    """Eliminate X instead of Y: explicit regime-indexed response schedule."""
    det = 1 - m.b * (m.a + k)
    if det == 0:
        raise ValueError('Undefined unique potential outcome')
    y = (m.d + v + m.b * (m.c + lam + u)) / det
    return m.c + lam + u + (m.a + k) * y, y

def iterate(m, u, v, lam, k, steps=100):
    """Simultaneous (Jacobi) adjustment, a separate convergence check."""
    x = y = 0.0
    for _ in range(steps):
        x, y = (float(m.c + lam + u) + float(m.a + k)*y,
                float(m.d + v) + float(m.b)*x)
    return x, y

def calibrate(mean_x, mean_y, clamp_slope, shift_slope):
    """Population moments from two specified interventions, not regression."""
    b = clamp_slope
    if b == 0 or shift_slope == 0:
        raise ValueError('Calibration requires nonzero responses')
    a = 1 / b - 1 / shift_slope
    return Model(a, b, mean_x - a*mean_y, mean_y - b*mean_x)

SHOCKS = tuple(product((F(-1), F(1)), repeat=2))

def observational_twin(m, alternative_a):
    mx, my = m.equilibrium()
    twin = Model(alternative_a, m.b, mx-alternative_a*my, m.d)
    shocks = tuple(twin.residuals(*m.equilibrium(u, v)) for u, v in SHOCKS)
    return twin, shocks

def average_y(m, shocks, lam=F(0), k=F(0)):
    return sum(m.equilibrium(u, v, lam, k)[1] for u, v in shocks) / len(shocks)

def results():
    m = Model()
    baseline = average_y(m, SHOCKS)
    shifts = {name: average_y(m, SHOCKS, lam, k)-baseline for name, lam, k in
              [('intercept', F(1), F(0)), ('responsiveness', F(0), F(1,5)),
               ('combined', F(1), F(1,5))]}
    twin, shocks = observational_twin(m, F(0))
    return {
        'study': 'E: simultaneous behavioral policy',
        'evidence': 'synthetic exact population laws; no empirical validation',
        'baseline_mean_xy': list(m.equilibrium()),
        'combined_policy_mean_xy': list(m.equilibrium(lam=F(1), k=F(1,5))),
        'mean_y_effects': shifts,
        'interaction': shifts['combined']-shifts['intercept']-shifts['responsiveness'],
        'clamp_x_unit_contrast': m.b,
        'individual_u1_vminus1_combined_effect':
            m.equilibrium(F(1), F(-1), F(1), F(1,5))[1]-m.equilibrium(F(1),F(-1))[1],
        'baseline_equivalent_twin_combined_effect':
            average_y(twin, shocks, F(1), F(1,5))-baseline,
        'known_or_calibrated_structure': 'congruent-informative; singleton 65/56',
        'baseline_only_invariant_linear_class': 'nonidentified; witnesses 65/56 and 65/72; not sharp bounds',
        'no_cross_policy_restrictions': 'sharp identified set R for mean contrast',
        'dag_only_original_variables': 'out-of-variant-scope for full intervention family',
        'policy_indexed_reduced_form_dag': 'congruent for policy interventions only',
        'framework_competition_demonstrated': False,
        'school_level_uncovered_domain_demonstrated': False,
    }

def serialized_results():
    return json.dumps(results(), default=lambda v: str(v) if isinstance(v, F) else v,
                      indent=2, sort_keys=True) + '\n'

if __name__ == '__main__':
    print(serialized_results(), end='')
