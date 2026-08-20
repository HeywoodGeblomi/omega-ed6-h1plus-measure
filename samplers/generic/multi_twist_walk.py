"""Discrete geometric multi-twist random walk on H1+ generators.

THIS IS NOT the continuous Masur–Veech / Rauzy–Veech measure.
It is a length-unweighted product of cylinder shears + the known 2:1
monodromy element. Reported only for side-by-side contrast with the
exact periodic orbit.

Harper: replace / extend with true continuous or Rauzy induction on
the pinned X(1,1) surface. Prefer sage-flatsurf if available.

promote_ready = false
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from certificates.qr_error_model import LyapEstimate, qr_lyapunov, report_side_by_side


def shear_h(k: float) -> np.ndarray:
    S = np.eye(4)
    S[0, 2] = k
    S[1, 3] = k
    return S


def shear_v(k: float) -> np.ndarray:
    S = np.eye(4)
    S[2, 0] = k
    S[3, 1] = k
    return S


def example_M() -> np.ndarray:
    return np.array(
        [[-15, 0, -2, 0], [0, 1, 0, -3], [8, 0, 1, 0], [0, 2, 0, -5]],
        dtype=float,
    )


def generators() -> list[np.ndarray]:
    M = example_M()
    gens = [
        shear_h(1), shear_h(2), shear_h(-1),
        shear_v(1), shear_v(2), shear_v(-1),
        M, np.linalg.inv(M),
        M @ shear_h(1),
        shear_v(1) @ M,
    ]
    J = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]], float)

    def ok(B):
        return (
            np.linalg.norm(B.T @ J @ B - J) < 1e-8
            and abs(np.linalg.det(B) - 1) < 1e-6
        )

    return [G for G in gens if ok(G)]


def run(n_steps: int = 20_000, seed: int = 7) -> LyapEstimate:
    gens = generators()
    rng = np.random.default_rng(seed)
    products = [gens[rng.integers(0, len(gens))] for _ in range(n_steps)]
    return qr_lyapunov(products)


def main() -> None:
    generic = run(20_000)
    periodic = LyapEstimate(
        values=(0.6667, 0.3333, -0.3333, -0.6667),
        err=(0.0, 0.0, 0.0, 0.0),
        steps=1,
        method="exact_orbit",
        notes="closed geodesic A; path-local",
    )
    print(report_side_by_side(periodic, generic))
    print()
    print("generic λ1+/λ2+:", generic.lambda1_plus, generic.lambda2_plus)
    print("generic ratio:", generic.ratio)
    s = generic.lambda1_plus + generic.lambda2_plus
    if s > 0:
        print("scaled to 6/7:", generic.lambda1_plus * (6 / 7) / s, generic.lambda2_plus * (6 / 7) / s)
    print()
    print("SCOPE: discrete multi-twist walk — NOT continuous Masur–Veech measure.")
    print("promote_ready: false")

    out = {
        "lambda1_plus": generic.lambda1_plus,
        "lambda2_plus": generic.lambda2_plus,
        "ratio": generic.ratio,
        "err": list(generic.err),
        "steps": generic.steps,
        "method": generic.method,
        "promote_ready": False,
    }
    dest = Path(__file__).resolve().parents[2] / "data" / "generic_multi_twist_walk.json"
    dest.write_text(json.dumps(out, indent=2))
    print("wrote", dest)


if __name__ == "__main__":
    main()
