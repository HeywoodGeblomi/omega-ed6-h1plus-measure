# Generic sampler (to build)

Long Rauzy / continuous Teichmüller paths intended to approximate the
Masur–Veech / EKZ invariant measure on the X(1,1) surface in $\Omega E_5(6)$.

## Requirements

- Pin the same residual-0 geometric basis used by the periodic sampler.
- Accumulate the Kontsevich–Zorich cocycle on $H_1^+$ along generic orbits.
- QR or interval error model on every Lyapunov estimate.
- Report both the generic spectrum and the periodic spectrum side-by-side.
  Disagreement is a result, not a bug to hide.

## Preferred external tools

Prefer talking to [sage-flatsurf](https://github.com/flatsurf/sage-flatsurf)
if it saves engineering time. Do not compete with it.

## Owner

Harper (measure sampler tech lead).
