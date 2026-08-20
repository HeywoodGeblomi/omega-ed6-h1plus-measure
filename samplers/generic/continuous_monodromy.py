"""Continuous-time geometric monodromy on H1+ generators.

Poisson switching among cylinder shears + the known 2:1 element M+.
QR Oseledets in continuous time. Multi-seed SE + 95% CI.

NOT full Gauss–Manin on a certified polygonal developing map.
promote_ready = false
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


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


def Mplus() -> np.ndarray:
    return np.array([[-15.0, 0, -2, 0], [0, 1, 0, -3], [8, 0, 1, 0], [0, 2, 0, -5]])


def generators() -> list[np.ndarray]:
    M = Mplus()
    gens = [
        shear_h(1), shear_h(2), shear_h(-1),
        shear_v(1), shear_v(2), shear_v(-1),
        M, np.linalg.inv(M),
        M @ shear_h(1), shear_v(1) @ M,
    ]
    J = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]], float)
    out = []
    for G in gens:
        if np.linalg.norm(G.T @ J @ G - J) < 1e-8 and abs(np.linalg.det(G) - 1) < 1e-6:
            out.append(G)
    return out


def fractional_shear(G: np.ndarray, frac: float) -> np.ndarray:
    if abs(frac) < 1e-12:
        return np.eye(4)
    D = G - np.eye(4)
    if np.linalg.norm(D @ D) < 1e-8:
        return np.eye(4) + frac * D
    return np.eye(4)


def continuous_path_lyapunov(T_max: float = 200.0, seed: int = 0, switch_rate: float = 1.0):
    rng = np.random.default_rng(seed)
    gens = generators()
    Q = np.eye(4)
    sums = np.zeros(4)
    t = 0.0
    switches = 0
    while t < T_max:
        G = gens[rng.integers(0, len(gens))]
        tau = min(rng.exponential(1.0 / switch_rate), T_max - t)
        n_full = int(math.floor(tau))
        frac = tau - n_full
        for _ in range(n_full):
            M = G @ Q
            Q, R = np.linalg.qr(M)
            signs = np.sign(np.diag(R)); signs[signs == 0] = 1
            Q = Q * signs
            R = (signs * R.T).T
            sums += np.log(np.abs(np.diag(R)) + 1e-300)
            t += 1.0
            switches += 1
            if t >= T_max:
                break
        if t >= T_max:
            break
        F = fractional_shear(G, frac)
        M = F @ Q
        Q, R = np.linalg.qr(M)
        signs = np.sign(np.diag(R)); signs[signs == 0] = 1
        Q = Q * signs
        R = (signs * R.T).T
        sums += np.log(np.abs(np.diag(R)) + 1e-300)
        t += frac
        switches += 1
    vals = sums / max(t, 1e-15)
    order = np.argsort(-vals)
    return vals[order], float(t), switches


def pack(x: np.ndarray) -> dict:
    se = float(x.std(ddof=1) / math.sqrt(len(x))) if len(x) > 1 else float("nan")
    return {
        "mean": float(x.mean()),
        "std": float(x.std(ddof=1)),
        "se": se,
        "ci95": [float(x.mean() - 1.96 * se), float(x.mean() + 1.96 * se)],
        "n": int(len(x)),
    }


def ensemble(n_seeds: int = 24, T_max: float = 400.0) -> dict:
    rows = []
    for s in range(n_seeds):
        vals, T, sw = continuous_path_lyapunov(T_max=T_max, seed=200 + s)
        pos = [float(v) for v in vals if v > 1e-6]
        rows.append({
            "seed": 200 + s,
            "T": T,
            "switches": sw,
            "values": [float(v) for v in vals],
            "lambda1": pos[0] if pos else float("nan"),
            "lambda2": pos[1] if len(pos) > 1 else float("nan"),
        })
    l1 = np.array([r["lambda1"] for r in rows], float)
    l2 = np.array([r["lambda2"] for r in rows], float)
    m = np.isfinite(l1) & np.isfinite(l2) & (l2 > 0)
    l1, l2 = l1[m], l2[m]
    ratio = l1 / l2
    s = float(l1.mean() + l2.mean())
    return {
        "method": "continuous-time Poisson switching on geometric Sp(4) + QR",
        "T_max": T_max,
        "n_seeds_valid": int(len(l1)),
        "lambda1": pack(l1),
        "lambda2": pack(l2),
        "ratio": pack(ratio),
        "scaled_to_6_7": [float(l1.mean() * 6 / 7 / s), float(l2.mean() * 6 / 7 / s)] if s > 0 else None,
        "periodic_contrast": {"ratio": 2.0, "scaled_to_6_7": [4 / 7, 2 / 7]},
        "error_model": "multi-seed mean ± SE; 95% CI (normal). Not interval arithmetic.",
        "promote_ready": False,
        "seeds": rows,
    }


def main() -> None:
    summary = ensemble(24, 400.0)
    print("λ1+", summary["lambda1"])
    print("λ2+", summary["lambda2"])
    print("ratio", summary["ratio"])
    print("scaled", summary["scaled_to_6_7"])
    print("promote_ready: false")
    dest = Path(__file__).resolve().parents[2] / "data" / "continuous_monodromy_ensemble.json"
    dest.write_text(json.dumps(summary, indent=2))
    print("wrote", dest)


if __name__ == "__main__":
    main()
