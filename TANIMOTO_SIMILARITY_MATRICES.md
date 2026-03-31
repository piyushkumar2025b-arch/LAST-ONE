# ⬡ ChemoFilter: Tanimoto Similarity & Jaccard Bitwise Math

**The Computational Heart of Molecular Fingerprinting**  
*Understanding the Intersection and Union of BitVectors (MORGAN/ECFP)*

---

## 1. Executive Overview

Cheminformatics does not "compare" strings (SMILES). It "compares" **BitVectors** (Morgan Fingerprints). **Tanimoto Similarity** (also known as the Jaccard Index) is the mathematical scalar (0.0 to 1.0) representing the structural overlap between two molecules. 

This document details the $O(1)$ bitwise core in `data_engine.py`.

---

## 2. Molecular Fingerprinting (MORGAN/ECFP4)

ChemoFilter uses **Morgan Fingerprints (Radius 2)** with a 2048-bit length.

1.  **Stage 1:** Each atom in the molecule is assigned an integer based on its properties (Element, Valence, H-count).
2.  **Stage 2 (Expansion):** The integer includes neighbors within a 2-bond radius ($Radius=2$), analogous to **ECFP4**.
3.  **Stage 3 (Hashing):** These integer codes are hashed into one of the 2,048 available bit positions.
4.  **Result:** A `11000101...` bitvector representation of the molecule.

---

## 3. The Tanimoto Equation (Bitwise)

To calculate the similarity between Molecule A and Molecule B:

$$T(A, B) = \frac{c}{a + b - c}$$

*   **$a$:** Number of bits set to 1 in Molecule A's fingerprint.
*   **$b$:** Number of bits set to 1 in Molecule B's fingerprint.
*   **$c$:** Number of "common" bits (Intersection) where both A and B have a 1 at the same position.

---

## 4. Performance: The $O(1)$ Bit-Count Advantage

Traditional SMILES-string comparison is slow. Tanimoto is extremely fast because:

1.  **Bitwise `AND`:** Calculation of $c$ is a single-clock instruction on modern CPUs (`A & B`).
2.  **`POPCNT`:** Counting the set bits ($a, b, c$) is a native hardware operation on x86_64 architecture (`POPCNT` instruction).
3.  **Result:** ChemoFilter can compare an unknown compound against the 200+ FDA-approved drugs in the `chemical_intelligence_db.py` in **sub-millisecond** time.

---

## 5. Thresholds & Clustering Interpretation

| Tanimoto Range | Classification | Scientific Meaning |
| :--- | :--- | :--- |
| **1.0** | Identical | The molecules share the exact same structural features. |
| **0.85 to 0.99** | Lead Family | Highly likely to share the same biological target and potency. |
| **0.6 to 0.85** | Structure Analogs | Candidates for **Bioisostere Replacement** or **Scaffold Morphing**. |
| **< 0.4** | Diverse | Structurally unrelated compounds. |

---

## 6. How to Use the Similarity Heatmap ($100 \times 100$)

The **"Analytical Dashboard"** uses the **Tanimoto Matrix** to generate the **Similarity Heatmap**. 

*   **Logic:** A darker cyan cell indicates a "Hit" where two molecules share a high Tanimoto value.
*   **Value:** Instant visualization of "Redundant Leads" in a large screening library.
