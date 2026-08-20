# Flatsurf Lyapunov approx on 8-square origamis in H(6)

**Status:** numerical consistency check. Not a theorem.

`promote_ready = false`

## Setup

- SageMath 10.7 + surface-dynamics / sage-flatsurf 0.8.0
- Query: `OrigamiDatabase().query(stratum=AbelianStratum(6), nb_squares=8)`
- Count: 16
- Call: `lyapunov_exponents_approx(nb_iterations=2**20, nb_experiments=8)`
- Output is `[\lambda_2, \lambda_3, \lambda_4]` (`\lambda_1 = 1` omitted)

These are **all** 8-square origamis in `H_4(6)`, not Prym-filtered.

Prym filter: no order-2 automorphism in `automorphism_group()`, and no involution `s` with `s r s = r` and `s u s = u`. Flatsurf `involution=` cannot split `H^\pm` on this set.

## Raw table

| r | u | \lambda2 | \lambda3 | \lambda4 | extra sum |
|---|---|----------|----------|----------|-----------|
| (1)(2)(3,4)(5,6)(7,8) | (1,2,3)(4,5)(6,7,8) | 0.72846 | 0.43803 | 0.11928 | 1.2858 |
| (1)(2)(3,4,5,6)(7,8) | (1,2,3)(4,6,7)(5)(8) | 0.73366 | 0.41535 | 0.13680 | 1.2858 |
| (1)(2)(3,4,5,6)(7,8) | (1,2,3)(4,7,6)(5)(8) | 0.73358 | 0.41547 | 0.13679 | 1.2858 |
| (1)(2)(3,4)(5,6,7,8) | (1,2,3)(4,5)(6,8)(7) | 0.73266 | 0.41472 | 0.13835 | 1.2857 |
| (1)(2)(3,4)(5,6)(7,8) | (1,2,3)(4,5)(6,7)(8) | 0.71797 | 0.43069 | 0.13703 | 1.2857 |
| (1)(2)(3,4)(5,6)(7,8) | (1,2,3)(4,5,6,7,8) | 0.44496 | 0.28569 | 0.12650 | 0.8572 |
| (1)(2)(3,4)(5)(6,7,8) | (1,2,3,5,6)(4,7)(8) | 0.45944 | 0.28706 | 0.11065 | 0.8572 |
| (1)(2)(3,4)(5,6,7,8) | (1,2,3,4,5,6,8)(7) | 0.48648 | 0.25773 | 0.11307 | 0.8573 |
| (1)(2)(3,4,5)(6,7,8) | (1,2,3,5,8,7)(4,6) | 0.44071 | 0.28577 | 0.13082 | 0.8573 |
| (1)(2)(3,4,5)(6,7,8) | (1,2,3,4,6,7)(5,8) | 0.44057 | 0.28566 | 0.13081 | 0.8570 |
| (1)(2)(3,4)(5,6)(7,8) | (1,2,3)(4,5,7)(6)(8) | 0.43957 | 0.28569 | 0.13178 | 0.8570 |
| (1)(2)(3,4)(5,6,7,8) | (1,2,3)(4,5)(6)(7,8) | 0.59738 | 0.27904 | 0.12334 | 0.9998 |
| (1)(2)(3,4)(5,6)(7,8) | (1,2,3,4,5)(6,7)(8) | 0.58614 | 0.29937 | 0.11440 | 0.9999 |
| (1)(2)(3,4,5)(6,7,8) | (1,2,3)(4)(5,6,8)(7) | 0.59038 | 0.28624 | 0.12341 | 1.0000 |
| (1)(2)(3,4,5)(6,7,8) | (1,2,3)(4)(5,6,7)(8) | 0.59040 | 0.28617 | 0.12322 | 0.9998 |
| (1)(2,3,4)(5,6,7)(8) | (1,2,3,5)(4,6,7,8) | 0.58557 | 0.27159 | 0.14285 | 1.0000 |

## Clusters vs Yu–Zuo on H(6)

| n | extra sum | typical triple | Yu–Zuo |
|---|-----------|----------------|--------|
| 5 | 9/7 | ~0.73, 0.42, 0.13 | hyp: 5/7, 3/7, 1/7 |
| 6 | 6/7 | ~0.45, 0.28, 0.13 | odd: 3/7, 2/7, 1/7 |
| 5 | 1 | ~0.59, 0.28, 0.13 | even: 4/7, 2/7, 1/7 |

Prym-Weierstrass loci sit in the even component (Möller). The even cluster is consistent with 4/7 + 2/7 + 1/7.

This is a Haar average on arithmetic Teichmüller curves of 8-square origamis, not the Prym-filtered split and not a proof of the individual exponents.

## Attribution

- Sum on each component: Yu–Zuo / EKZ
- Prym containment in even: Möller
- Individual values on the components: Yu–Zuo
- This table: computational consistency only
