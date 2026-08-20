# Status — omega-ed6-h1plus-measure

**One job:** error-barred Masur–Veech average of $\lambda_1^+,\lambda_2^+$ on $H_1^+$ for $\Omega E_D(6)$.

`promote_ready = false`

## Locked side-by-side

| sampler | $\lambda_1^+$ | $\lambda_2^+$ | ratio |
|---------|---------------|---------------|-------|
| periodic exact $A$ (path-local) | $2/3$ | $1/3$ | 2.00 → scales to $4/7,2/7$ |
| continuous geometric (24×T=400) | $0.647\pm 0.015$ | $0.400\pm 0.009$ | 1.623 CI$_{95}$ $[1.57,1.67]$ |
| **X(2,0) cylinder moduli** | $0.456\pm 0.001$ | $0.456\pm 0.001$ | **1.00** |

Scaled continuous (prior gens) $\approx 0.530/0.327$ — away from $4/7+2/7$.
X(2,0) pure cylinders isotropic — result, not a bug.

## Literature correction

$\Omega E_5(6)=\mathrm{SL}(2,\mathbb{R})\cdot B(3,5)$. First generic X-prototype pin: **X(2,0)** for $D=8$ (`data/x20_prototype.json`).

## Gates

1. Developing-map / true Rauzy monodromy on pinned polygon (Harper).
2. Interval or explicit QR remainder (Lucas) — batch-means SE is live but not sufficient.
