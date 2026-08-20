# Status — omega-ed6-h1plus-measure

**One job:** error-barred Masur–Veech / EKZ average of $\lambda_1^+,\lambda_2^+$ on $H_1^+$ for $\Omega E_5(6)$.

`promote_ready = false`

## Side-by-side (latest)

| sampler | $\lambda_1^+$ | $\lambda_2^+$ | ratio | notes |
|---------|---------------|---------------|-------|-------|
| periodic (exact orbit $A$) | $2/3$ | $1/3$ | $2.00$ | path-local; scaled → $4/7,2/7$ |
| discrete multi-twist walk (20k) | $\approx 0.901$ | $\approx 0.463$ | $\approx 1.94$ | geometric gens |
| **continuous-time geometric** (24 seeds × T=400) | $0.647 \pm 0.015$ | $0.400 \pm 0.009$ | $1.623$ CI$_{95}$ $[1.57,1.67]$ | Poisson switching on same gens |

Scaled continuous positives to sum $6/7$: $\approx 0.530 / 0.327$ (not $4/7,2/7$).

## Error model

Multi-seed mean ± SE and normal 95% CI are live. Interval / ball arithmetic and rigorous QR remainders are **not** live yet (see `certificates/error_model.md`).

## Scope honesty

- Continuous-time path is geometric monodromy on the known Sp(4) generators, **not** Gauss–Manin on a certified polygonal developing map.
- Pure Rauzy length cocycle on a schematic 4-IET is parabolic (one exponent) — as expected; it is not the KZ cocycle on $H_1^+$.
- Scaling to $6/7$ is display only.

## Next gates

1. Harper: Rauzy / continuous monodromy from a **pinned polygonal / zippered X(1,1)** (prefer sage-flatsurf).
2. Lucas: interval or explicit QR-remainder bounds replacing normal-approx CI.
3. Only then discuss whether the average sits on $4/7+2/7$ or kills the conjecture.
