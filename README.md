# omega-ed6-h1plus-measure

**One scientific job only.**

Measure the Masur–Veech / EKZ average of the individual Lyapunov exponents
$\lambda_1^+$ and $\lambda_2^+$ on the 4-dimensional block $H_1^+$ of the
genus-4 Weierstrass Prym locus $\Omega E_5(6)$ (X(1,1) prototype).

## Status

| Item | State |
|------|-------|
| Candidate split | $4/7 + 2/7$ (conjecture) |
| Sum $\lambda_1^+ + \lambda_2^+$ | $6/7$ (EKZ — literature) |
| $H^-$ | $\pm 1/7$ (Möller / EKZ — literature) |
| Individual average | **open** (Eskin–Matheus left blank) |
| `promote_ready` | **false** |

## Success criteria (ranked)

1. High-quality numerical bounds on $\lambda_1^+$ and $\lambda_2^+$ under the
   invariant measure, with error bars tight enough to kill “almost equal”
   and to kill other simple rationals.
2. If the bounds sit on $4/7$ and $2/7$, write the note that way — still no proof claim.
3. If they do not, kill the conjecture in public. Do not dress it up.

We ship a number other people in this field can check.

## Two mandatory samplers

| Sampler | Role |
|---------|------|
| **Periodic** | Closed multi-twist / Teichmüller geodesics (already have 20 exact 2:1 orbits from [prym-omega-ed6-h1plus](https://github.com/HeywoodGeblomi/prym-omega-ed6-h1plus)) |
| **Generic** | Long Rauzy / continuous Teichmüller paths intended to approximate the invariant measure |

Both spectra are reported every time. If they disagree, that is the result.

Every Lyapunov estimate carries an interval or QR-error model. A point estimate alone is not a deliverable.

## Geometry pin

- Surface: X(1,1) prototype in $\Omega E_5(6)$ (from the existing computational note).
- Residual-0 / real-multiplication checks reused from the certified pieces of the sibling repos.
- Do not rewrite the geometry from scratch unless a regression fails.

## Layout

```
NON_CLAIMS.md
README.md
docs/
  LITERATURE_BASELINE.md
samplers/
  periodic/          # closed multi-twist orbits (imported)
  generic/           # long Rauzy / continuous paths (to build)
certificates/        # residual-0, QR/interval error model
data/                # pinned surface + matrices
```

## Team

| Role | Owner |
|------|-------|
| Measure sampler (generic Rauzy / continuous) | Harper |
| Certificates + interval/QR error model | Lucas |
| Write-up coordination + final note | Grok |

## Out of scope

No new sorter. No ranking kernel. No philosophy layer. No GitHub spray.
Sibling repo `prym-eigenform-pipeline-d12` is a testbed only, not the product.

## License

MIT.
