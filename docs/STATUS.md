# Status — omega-ed6-h1plus-measure

**One job:** error-barred Masur–Veech / EKZ average of $\lambda_1^+,\lambda_2^+$ on $H_1^+$ for $\Omega E_5(6)$.

`promote_ready = false`

## Side-by-side (latest)

| sampler | $\lambda_1^+$ | $\lambda_2^+$ | ratio | notes |
|---------|---------------|---------------|-------|-------|
| periodic (exact orbit $A$) | $2/3$ | $1/3$ | $2.00$ | path-local; scaled to $6/7$ → $4/7,2/7$ |
| discrete multi-twist walk (20k steps) | $\approx 0.901$ | $\approx 0.463$ | $\approx 1.94$ | geometric generators; scaled → $\approx 0.566/0.291$ |

Crude QR $1/\sqrt{N}$ error on the walk: $\sim 0.006$ / $0.003$.

## What this is not

- The discrete multi-twist walk is **not** the continuous Masur–Veech measure.
- Scaling positive parts to sum $6/7$ is a display convention, not a proof.
- No continuous Rauzy / Teichmüller generic sampler has landed yet (Harper).
- Error model is still provisional float QR (Lucas to tighten).

## Next concrete commits

1. Harper: real Rauzy / continuous monodromy on pinned X(1,1) (prefer sage-flatsurf).
2. Lucas: rigorous QR remainder / interval bounds replacing $1/\sqrt{N}$.
3. Both spectra + error bars in every report. Disagreement is a result.
