# ⬡ ChemoFilter: Algorithmic & Mathematical Theory

This document explicitly outlines the mathematical equations hard-coded into `chemo_scoring.py` to evaluate physicochemical viability. It serves as proof of the platform's rigour beyond simple structural mapping.

---

## 1. The Lead Score Algorithm
The `LeadScore` is not a theoretical AI guess; it is a deterministic scalar (0-100) generated through asymmetrical penalty functions.

**Equation:**
`LeadScore = (QED × 26) + Vc_{bonus} + ADME_{bonus} + (Sim × 13) - Tox_{penalty} - SA_{penalty} - CYP_{penalty}`

**Variables:**
*   $QED \in [0, 1]$
*   $Vc_{bonus}$: Up to 20 points based on Lipinski compliance (`max(0, 4 - Violations) × 5`)
*   $ADME_{bonus}$: +14 if HIA (Stomach Absorbed), +9 if BBB (Brain Penetrant)
*   $Sim$: Tanimoto Similarity index against the target profile (0 to 1).
*   $Tox_{penalty}$: -10 for PAINS alert, -12 for HIGH hERG Risk.
*   $SA_{penalty}$: Scales exponentially based on synthetic accessibility index.
*   $CYP_{penalty}$: -2 for every targeted cytochrome P450 isoenzyme.

## 2. ESOL Aqueous Solubility (logS)
We replicate the Delaney equation natively inside RDKit without external web calls.

**Equation:**
`logS = 0.16 - 0.63(LogP) - 0.0062(MW) + 0.066(RotBonds) - 0.74(Aromatics / HeavyAtoms)`

*   A calculated $logS > -4$ is considered moderately soluble. 
*   Below $-6$ triggers an "Insoluble" UI warning.

## 3. Synthetic Accessibility (SA_Score)
We calculate SA internally by analysing fragment complexity and stereocenter density.

**Equation:**
`SA = 1 + (Rings × 0.4) + (StereoCenters × 0.8) + (HeavyAtoms / 30) + (AromaticRings × 0.3)`
*(Multiplied by a proprietary complexity factor of 1.25 if macrocycles are detected).*

## 4. Tanimoto Similarity (Jaccard Index)
When graphing the `_fp` (Molecular Fingerprints), the UI calculates the bitwise intersection of two Morgan Fingerprint BitVectors.
`Tanimoto(A, B) = c / (a + b - c)`
Where:
* $a$ = Number of bits set to 1 in A (2048-bit radius 2)
* $b$ = Number of bits set to 1 in B
* $c$ = Number of intersecting bits between A and B.

This $O(1)$ bitwise operation allows the platform to generate a 10,000x10,000 similarity heatmap matrix in under 2 seconds.
