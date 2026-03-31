# ⬡ ChemoFilter: Mutagenicity & Ames Test Logic

**Predicting DNA-Interactions and Genetic Toxicity**  
*The High-Resolution Genetic Hazard Gateway of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

**Mutagenicity** is the potential for a compound to cause genetic damage (mutations). **ChemoFilter** uses structural fingerprints and structural alerts to predict the mutagenic potential, mapping results to the Ames Test (Salmonella Typhimurium).

---

## 2. Defining Mutagenicity Categories

ChemoFilter classifies leads into one of two **Mutagenicity Categories** based on predicted Ames Test results ($S9 +/-$):

| Category | Predicted Result | Interpretation |
| :--- | :--- | :--- |
| **Active** | **Ames Positive.** | **High Mutagenic Risk.** Potential carcinogen. |
| **In-Active** | **Ames Negative.** | **Non-Mutagenic.** Safe for initial research. |

---

## 3. The 3-Step Mutagenicity Prediction Sequence

When a lead enters Tier 7 (**Celestial Engine**):

1.  **Structure-Activity Mapping:** The system extracts the **Morgan Fingerprint** and identifies known "Genotoxic Alerts" (e.g., specific alkylating agents).
2.  **Regression Analysis:** Calculation of the mutagenic probability using a multi-linear model trained on the **Ames** database.
3.  **Result Display:** A 🔴 **"High Mutagenicity Warning"** is triggered if the predicted mutagenic probability is over 0.5.

---

## 4. Visualizing Hazard: The "Genotoxicity Dashboard"

The UI features a **"Mutagenic Hazard Table"** where:

*   **Logic:** Automatic color-coding based on the mutagenicity category.
*   **Result:** A chemist can see at a glance if their lead is "Ames Positive" or "Ames Negative."
*   **Actionable Insight:** If a molecule is "Ames Positive," the system suggests the **"Scaffold Morph"** module to mitigate the structural alerts.

---

## 5. Significance in Early Drug Discovery

An **Ames Positive** lead is rarely progressed to Phase I clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **Tox21** datasets to provide quantitative mutagenic probabilities for different organ systems (e.g., Hepatic vs. Renal).
