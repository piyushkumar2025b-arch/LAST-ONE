# ⬡ ChemoFilter: Chirality & 3D Stereochemistry Handling

**The Science of "Handedness" in Drug Molecules**  
*Understanding Tier 9 (Aether Engine) Isomerism and Conformer Search*

---

## 1. Executive Overview

In pharmacology, **Chirality** (the existence of mirror-image $R$ and $S$ enantiomers) is critical. A classic example is Thalidomide, where one enantiomer is a sedative and the other is a teratogen. 

**ChemoFilter** handles chirality by moving from 2D SMILES to 3D Conformer Analysis in its **Tier 9 (Aether Engine)**.

---

## 2. Defining Chirality (@ and @@ Notations)

ChemoFilter uses the RDKit C++ kernel to parse chiral SMILES:

*   `@`: Anti-clockwise (S)
*   `@@`: Clockwise (R)

**Logic:** If the user provides a "Chiral-capable" SMILES but does *not* specify the chirality (e.g., `CC(O)C`), ChemoFilter will automatically generate a **Racemic Mixture** for its ADMET calculations and pick the most energetically stable form for 3D rendering.

---

## 3. Geometric Isomerism (E/Z Notations)

Double bond configurations are equally handled:

*   `E` (Entgegen): Opposite sides (Trans-like).
*   `Z` (Zusammen): Same side (Cis-like).

**Lead Score Impact:** If a molecule's **E/Z configuration** forces a steric clash in its 3D minimized state (Tier 9), the system will apply a **"Conformer Strain Penalty"** to the final `Lead_Score`.

---

## 4. Conformer Generation (ETKDG v3)

Tier 9 uses the **Experimental-Torsion Knowledge Distance Geometry (ETKDG)** method (v3, 2020) to generate the most physically realistic 3D shape.

1.  **3D Embedding:** `rdDistGeom.EmbedMolecule`.
2.  **Force-Field Minimization:** Merck Molecular Force Field (**MMFF94**).
3.  **Result:** A realistic 3D Cartesian representation of the drug.

---

## 5. Visualizing Chirality: The "3D Explorer"

The UI features a **"3D Conformer Explorer"** tab (Plotly/py3Dmol) where:

*   **Chiral Centers:** Marked with a subtle glowing halo.
*   **Rotation:** A user can "Spin" the molecule to verify if a side-group points "Into the page" or "Out of the page." 

---

## 6. Future: Pro-Chirality & Metabolic Reactivity

Phase 4 (Roadmap) includes **Pro-Chiral Centers**, which identifies molecules that are not chiral but could *become* chiral through metabolic oxidation in the liver (e.g., $CH_2$ to $CH(OH)$).
