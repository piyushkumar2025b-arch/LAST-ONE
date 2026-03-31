# ⬡ ChemoFilter: Molecular Docking Setup & Simulation Parameters

**The Technical Guide to In Silico Receptor-Ligand Binding**  
*Preparing Leads for External Docking Engines (AutoDock Vina, LeDock)*

---

## 1. Executive Overview

While ChemoFilter provides rapid **2D Similarity Triage**, the ultimate validation of a drug candidate is its binding affinity to a specific protein target. This document details how to prepare leads from ChemoFilter for high-resolution **Molecular Docking** simulations.

---

## 2. Preparing the Ligand (From SMILES)

Before docking, the "2D String" (SMILES) must be converted to a "3D File" (.PDBQT or .MOL2).

1.  **3D Minimization:** ChemoFilter's **Tier 9 (Aether Engine)** uses the **MMFF94** force field to generate the lowest-energy conformer.
2.  **Protonation:** All molecules are "Protonated at pH 7.4" (Physiological pH) to ensure Nitrogen atoms are in their correct ionic state using `AllChem.EmbedMolecule`.
3.  **Partial Charges:** Calculation of **Gasteiger Charges** to model the electrostatic interaction between the ligand and the receptor.

---

## 3. AutoDock Vina Integration Parameters

If you are using the integrated **Vina-Wrapper**, the following default settings are applied:

| Parameter | Default Value | Significance |
| :--- | :--- | :--- |
| **Exhaustiveness** | 8 | Balance between speed and binding search depth. |
| **Energy Range** | 3.0 kcal/mol | Only record conformers within 3kcal of the global minimum. |
| **CPU Threads** | Auto-Detect | Utilizes all available local cores for multi-conformational search. |
| **Box Center** | $X, Y, Z$ | Centered on the geometric median of the target's active site. |

---

## 4. Defining the "Search Space" (Grid Box)

To docking successfully, the search must be restricted to the target protein's active site (The Pocket).

*   **Size:** Usually $20\text{\AA} \times 20\text{\AA} \times 20\text{\AA}$ to encompass the entire binding pocket.
*   **Spacing:** $0.375\text{\AA}$ (The gold standard for AutoDock Vina).

---

## 5. Interpreting Docking Results (Binding Affinity)

The output is provided as a **$\Delta G$ (Gibbs Free Energy)** value in $kcal/mol$.

*   **$\Delta G < -8.0 kcal/mol$:** Excellent Lead. High probability of receptor binding.
*   **$-6.0$ to $-8.0 kcal/mol$:** Moderate Lead. May require scaffold optimization.
*   **$>-5.0 kcal/mol$:** Poor Lead. Likely a "Non-Specific Binder" or has steric clashes.

---

## 6. How to Run Batch Docking

ChemoFilter’s **"Docking Suite"** (Phase 6) allows you to select the "Top 5 Leads" and automatically launch 5 parallel docking simulations against a user-uploaded .PDB protein structure, with results rendered directly in the **3D Force-Field Explorer**.
