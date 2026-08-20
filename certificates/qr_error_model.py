"""Provisional QR-error / remainder skeleton for Lyapunov estimates.

Every estimate — periodic or generic — must call this (or a stricter
interval model) before it is recorded as a deliverable.

Owner: Lucas. promote_ready remains false until the measure average is pinned.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class LyapEstimate:
    """Point spectrum + provisional error bars on the positive parts."""

    values: tuple[float, ...]          # ordered Lyapunov exponents
    err: tuple[float, ...]             # absolute error bars (same length)
    steps: int
    method: str                        # "qr_float" | "interval" | "exact_orbit"
    notes: str = ""

    @property
    def lambda1_plus(self) -> float:
        pos = [v for v in self.values if v > 0]
        return float(pos[0]) if pos else float("nan")

    @property
    def lambda2_plus(self) -> float:
        pos = sorted((v for v in self.values if v > 0), reverse=True)
        return float(pos[1]) if len(pos) > 1 else float("nan")

    @property
    def ratio(self) -> float:
        a, b = self.lambda1_plus, self.lambda2_plus
        if b == 0 or not np.isfinite(b):
            return float("nan")
        return a / b


def qr_lyapunov(
    products: Sequence[np.ndarray],
    *,
    renorm_every: int = 50,
) -> LyapEstimate:
    """Oseledets via repeated QR on a list of Sp(4)-valued steps.

    products[i] is the monodromy matrix for step i (4x4).
    Returns mid-point estimates with a crude remainder proxy:
        err_i ≈ |log σ_i| / sqrt(N)
    This is NOT a rigorous interval. Lucas must replace with ball/QR
    remainder bounds before any promotion discussion.
    """
    if not products:
        raise ValueError("empty product list")

    dim = products[0].shape[0]
    Q = np.eye(dim)
    sums = np.zeros(dim)
    n = 0

    for k, B in enumerate(products):
        M = B @ Q
        Q, R = np.linalg.qr(M)
        # force positive diagonal for continuous branch
        signs = np.sign(np.diag(R))
        signs[signs == 0] = 1.0
        Q = Q * signs
        R = (signs * R.T).T
        sums += np.log(np.abs(np.diag(R)) + 1e-300)
        n += 1
        if renorm_every and (k + 1) % renorm_every == 0:
            # Q already orthonormal; nothing else required for float path
            pass

    vals = tuple(float(x) for x in (sums / max(n, 1)))
    # crude statistical proxy — replace with rigorous model
    err = tuple(float(abs(v) / np.sqrt(max(n, 1))) for v in vals)
    return LyapEstimate(
        values=vals,
        err=err,
        steps=n,
        method="qr_float",
        notes="provisional; not interval-certified",
    )


def report_side_by_side(
    periodic: LyapEstimate,
    generic: LyapEstimate,
) -> str:
    """Mandatory report format: both spectra + error bars."""
    lines = [
        "| sampler   | λ1+        | λ2+        | ratio   | steps | method     |",
        "|-----------|------------|------------|---------|-------|------------|",
    ]
    for name, est in (("periodic", periodic), ("generic", generic)):
        lines.append(
            f"| {name:<9} | {est.lambda1_plus:10.6f} | {est.lambda2_plus:10.6f} |"
            f" {est.ratio:7.3f} | {est.steps:5d} | {est.method:<10} |"
        )
        lines.append(
            f"| {name+' err':<9} | ±{est.err[0] if est.err else float('nan'):9.6f} |"
            f" ±{est.err[1] if len(est.err)>1 else float('nan'):9.6f} |         |       |            |"
        )
    lines.append("")
    lines.append("promote_ready = false until interval/QR remainder is rigorous and average is pinned.")
    return "\n".join(lines)
