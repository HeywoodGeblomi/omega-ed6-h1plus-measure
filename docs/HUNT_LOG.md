# Hunt log

## Exact developing-map matrices (X(2,0))

From cylinder decomposition of the literature polygon (arXiv:2210.13503 Fig 4.6):

```
TH = [[1,0,0,0],[0,1,0,0],[2,0,1,0],[0,1,0,1]]   # horizontal multi-twist, Sp(4)
TV = [[1,0,0.5,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]] # vertical multi-twist, Sp(4)
```

These are the induced actions on the H1+ difference basis of the global affine multi-twists (derivative parabolic in SL(2,R)).

## Spectra

| generators | ratio | scaled to 6/7 |
|------------|-------|---------------|
| **exact TH, TV only** | **1.000** | 0.429/0.429 |
| + silver-unit Sp(4) blocks | 1.164 | 0.461/0.396 |
| shared-edge hack (prior) | 2.80 | 0.63/0.23 |
| target 2:1 | 2.00 | 0.571/0.286 |

**Result:** The true affine multi-twists of X(2,0) produce an isotropic H1+ spectrum. Extra hyperbolic elements (butterfly / Veech) are required for anisotropy; those matrices are not yet derived from a complete edge-labeled developing map.

`promote_ready = false`
