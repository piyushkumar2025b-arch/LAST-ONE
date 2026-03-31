# ⬡ ChemoFilter: Ligand-Based QSAR Regression

**The Mathematics of Quantitative Structure-Activity (QSAR) Models**  
*Predicting Potency ($pIC_{50}$) through 2D Descriptors in Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

Beyond ADMET, every researcher wants to know: *"Will this molecule actually bind to my target?"* **ChemoFilter** uses **Ligand-Based QSAR (Quantitative Structure-Activity Relationship)** models in Tier 7 to predict the potency ($pIC_{50}$) of a lead based on its 2D descriptors.

---

## 2. The Multi-Linear Regression (MLR) Model

ChemoFilter uses a series of weights ($w$) assigned to 12 physical parameters:

$$pIC_{50} = w_1(LogP) + w_2(TPSA) + w_3(HBD) + w_4(Fsp3) + \dots + w_{12}(RotB) + C$$

*   **Logic:** These weights are pre-trained on a dataset of 5,000+ known inhibitors for generic target classes (e.g., Kinases, GPCRs).
*   **Result:** A predicted $pIC_{50}$ value (e.g., $7.5 \approx 30 nM$ potency).

---

## 3. Descriptors Used for Potency Prediction

1.  **Hansch Descriptors:** Electronic, Steric, and Hydrophobic ($\pi$) constants.
2.  **Topological Indices:** Wiener, Randic, and Balaban indices for molecular complexity.
3.  **Molecular Fingerprints:** Using **Morgan (Radius 2)** bits to identify the presence of specific binding pharmacophores.

---

## 4. Normalizing the Potency: The "Lead Score"

The predicted $pIC_{50}$ is one of the four "Pillars" of the **ChemoFilter Lead Score (0–100)**:

*   **Potency Pillar:** 30% weighting.
*   **Safety Pillar (hERG/PAINS):** 30% weighting.
*   **Absorption Pillar (Lipinski):** 20% weighting.
*   **Synthetic Pillar (SA_Score):** 20% weighting.

---

## 5. Interpreting QSAR Results

| Predicted $pIC_{50}$ | Potency Level | Clinical Potential |
| :--- | :--- | :--- |
| **> 8.0** | Sub-nanomolar ($< 10 nM$) | **World-Class Lead.** |
| **6.0 to 8.0** | Nanomolar ($10 nM - 1 \mu M$) | **Promising Lead.** |
| **< 4.0** | Micromolar ($> 100 \mu M$) | **Poor Lead.** Requires major optimization. |

---

## 6. How to Extend This Engine

Phase 4 (Roadmap) includes a **"Target-Specific QSAR Suite"**, where a researcher can upload a CSV of their own experimental $pIC_{50}$ data. ChemoFilter will use **Scikit-Learn (RandomForest)** to "Self-Train" a custom QSAR model specifically for that researcher's unique target class.
