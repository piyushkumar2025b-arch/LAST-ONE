# ⬡ ChemoFilter: Pharmacophore Alignment & 3D Matching Logic

**The Science of "Superimposing" Molecular Points of Interest**  
*The Geometrical Principles behind Tier 9 (Aether Engine) Target Matching*

---

## 1. Executive Overview

A **Pharmacophore** is the abstract "3D representation" of the functional groups in a drug that are needed for receptor binding. **ChemoFilter** uses structural fingerprints and 3D minimization to identify if a lead's pharmacophore aligns with a known "Reference Lead."

---

## 2. Defining Pharmacophore "Feature Points"

ChemoFilter identifies six core features across every 3D conformer in **Tier 9**:

1.  **H-Bond Donors (HBD):** $NH_2, OH$ centers.
2.  **H-Bond Acceptors (HBA):** $O, N$ centers.
3.  **Hydrophobic Clusters (HPHO):** Aliphatic chains.
4.  **Aromatic Rings (AROM):** Phenyl, Pyridine rings.
5.  **Cationic (POS):** Basic centers ($pH=7.4$).
6.  **Anionic (NEG):** Acidic centers ($pH=7.4$).

---

## 3. The "RMSD" (Root-Mean-Square Deviation) Metric

To compare two molecules in 3D:

*   **Logic:** Align the **Pharmacophore Centers** of Molecule A and Molecule B.
*   **Result (RMSD):** The average distance between corresponding points in Ångströms ($\text{\AA}$).
*   **Significance:** An $RMSD < 1.0 \text{\AA}$ indicates a "Surgical Match"—the leads likely bind to the same target pocket.

---

## 4. Visualizing Alignment: The "3D Phantom Overlay"

The **"3D Conformer Explorer"** tab in `app.py` includes a **"Reference Overlay"** mode where:

*   **Molecule A (Reference):** Rendered as a transparent ghost ($Opacity=0.3$).
*   **Molecule B (Lead):** Rendered as a solid stick-model.
*   **Visual Check:** The chemist can see if their side-groups $OH$ and $NH_2$ physically overlap in 3D space with the proven drug.

---

## 5. Fractional Similarity ($F_{sim}$)

Beyond RMSD, ChemoFilter calculates $F_{sim}$ (Fractional Similarity) based on the **Shape Tanimoto Index**:

$$S_{shape} = \frac{V_{overlap}}{V_{A} + V_{B} - V_{overlap}}$$

*(Where $V$ is the Volume of the molecule).*

---

## 6. How to Optimize Your Alignment

If your lead has **"Poor 3D Alignment"**:
1.  **Rigidify the Scaffold:** Add a ring system to lock the pharmacophore points into place.
2.  **Stereoisomer Selection:** Switch from the $R$ to the $S$ enantiomer in the **SMILES input** to see if the mirror-image alignments improve.
3.  **Bioisostere Replacement:** Swap an $OH$ for an $NH_2$ if the donor/acceptor distance needs to be slightly shifted based on the **Celestial Engine** Tier.
