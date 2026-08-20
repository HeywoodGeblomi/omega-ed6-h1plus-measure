# Hunt log

## Literature pin

| Fact | Source |
|------|--------|
| $\Omega E_5(6)=\mathrm{SL}(2,\mathbb{R})\cdot B(3,5)$ | arXiv:2210.13503 |
| Generic $D>5$: $X(w,e)$, $D=e^2+4w$ | same Fig 4.6 |
| $X(2,0)$: two $\lambda/2$-squares + two $(w/2)\times(1/2)$ rectangles, $\lambda=\sqrt{2}$ | constructed |

## Geometric returns

| Sampler | ratio | scaled to $6/7$ |
|---------|-------|------------------|
| Periodic exact $A$ (path-local) | 2.00 | $4/7,2/7$ |
| Continuous geometric gens | 1.623 CI$[1.57,1.67]$ | $\approx 0.53/0.33$ |
| X(2,0) equal cylinder moduli | 1.00 | $0.43/0.43$ |
| **X(2,0) unequal long/short multi-twists** | **1.392 CI$[1.388,1.396]$** | **$\approx 0.50/0.36$** |

Unequal long/short moduli on the literature polygon break isotropy and produce stable off-diagonal coupling ($\|\mathrm{coupling}\|\approx 16.7$). Still not $4/7+2/7$. Result, not a bug.

## Gates remaining

1. Full edge-labeled developing map + genuine Rauzy/Gauss–Manin (not only multi-twist products).
2. Interval / explicit QR remainder (batch-means live).

`promote_ready = false`
