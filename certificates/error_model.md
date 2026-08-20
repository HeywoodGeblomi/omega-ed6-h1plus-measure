# Error model (current)

## What we ship

| Layer | Method | Status |
|-------|--------|--------|
| Point spectrum | QR Oseledets on Sp(4) products | live |
| Multi-seed SE | std / √n across independent seeds | live |
| 95% CI | normal approx mean ± 1.96 SE | live |
| Batch means | optional within-path blocks | recorded |
| Interval / ball arithmetic | — | **not yet** |
| Rigorous QR remainder bounds | — | **not yet** |

## What is required before promote_ready

1. Interval or ball enclosure on each Lyapunov exponent, **or**
2. Documented QR remainder bound with explicit constants,
3. **and** a continuous / Rauzy sampler tied to a certified polygonal developing map of X(1,1), not only generator products.

A multi-seed SE is necessary but not sufficient for a field-checkable claim.

## Owner

Lucas — tighten toward interval/QR remainder. Harper — polygonal continuous monodromy.
