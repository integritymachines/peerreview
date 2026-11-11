#!/usr/bin/env python3
"""Toy-model reference calculations; no inference engine or API calls."""
from dataclasses import dataclass
from math import isclose
import json

@dataclass(frozen=True)
class Interval:
    lower: float
    upper: float
    def __post_init__(self):
        if self.lower > self.upper:
            raise ValueError("empty identified set")
    def to_dict(self):
        return {"lower":self.lower,"upper":self.upper}

def relation(a,b,tol=1e-10):
    if isclose(a.lower,b.lower,abs_tol=tol) and isclose(a.upper,b.upper,abs_tol=tol):
        return "congruent"
    if a.upper < b.lower-tol or b.upper < a.lower-tol:
        return "incompatible"
    if a.lower >= b.lower-tol and a.upper <= b.upper+tol:
        return "a-refines-b"
    if b.lower >= a.lower-tol and b.upper <= a.upper+tol:
        return "b-refines-a"
    return "compatible-divergence"

def randomized_additive(tau=1.25):
    po=(tau+0)-0
    scm=tau*1-tau*0
    se=tau
    return {"case":"randomized_additive","estimand":"ATE","po":po,"scm":scm,"se":se,"relation":"congruent-informative"}

def confounded_twins():
    # Same P(A,Y); distinct do(A) contrasts.
    U=[0,1]
    m1=sum((1-0) for _ in U)/len(U)
    m2=sum((u-u) for u in U)/len(U)
    return {"case":"confounded_twins","observational_joint":[[.5,0.0],[0.0,.5]],
            "compatible_ate_examples":[m2,m1],
            "finding":"nonidentified: identified set contains both examples"}

def benefit_bounds(p_y1=.7,p_y0=.3):
    overlap_lo=max(0.0,p_y1+p_y0-1)
    overlap_hi=min(p_y1,p_y0)
    bounds=Interval(p_y1-overlap_hi,p_y1-overlap_lo)
    return {"case":"benefit_bounds","ate":p_y1-p_y0,
            "benefit_without_crossworld_assumption":bounds.to_dict(),
            "benefit_with_monotonicity":p_y1-p_y0}

def simultaneous_feedback(a=.4,b=.5):
    d=1-a*b
    if abs(d)<1e-12:
        raise ValueError("unique equilibrium not guaranteed")
    return {"case":"simultaneous_feedback","a":a,"b":b,
            "effect_of_policy_intercept_shift":b/d,
            "effect_of_do_X":b,
            "warning":"Different interventions: not a framework disagreement"}

def results():
    return {"status":"formal illustrative toy calculations, not empirical validation",
            "cases":[randomized_additive(),confounded_twins(),benefit_bounds(),simultaneous_feedback()],
            "framework_exclusive_win_demonstrated":False,
            "school_level_uncovered_domain_demonstrated":False}

if __name__=="__main__":
    print(json.dumps(results(),sort_keys=True,indent=2))
