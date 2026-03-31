# ⬡ ChemoFilter: Blood-Brain Barrier (BBB) Penetration Models

**Predicting CNS Activity and Brain Permeability**  
*The Neuroscience Gateway of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

**Blood-Brain Barrier (BBB) Penetration** is the critical factor for drugs targeting the Central Nervous System (CNS). **ChemoFilter** uses structural fingerprints and logP/TPSA correlations to predict the brain-permeability potential.

---

## 2. Defining BBB Penetration Categories

ChemoFilter classifies leads into one of two **BBB Penetration Categories** based on predicted LogBB values ($log([Brain]/[Plasma])$):

| Category | LogBB Range | Interpretation |
| :--- | :--- | :--- |
| **P⁺** | $\geq 0$ | **BBB Penetrant.** Potential CNS drug. |
| **P⁻** | $< 0$ | **Non-Penetrant.** Peripheral drug only. |

---

## 3. The 3-Step BBB Prediction Sequence

When a lead enters Tier 7 (**Celestial Engine**):

1.  **Structure-Activity Correlation:** The system extracts the **LogP** and **TPSA** (Topological Polar Surface Area).
2.  **Regression Analysis:** Calculation of the LogBB value using a multi-linear model trained on the **BDB** database.
3.  **Result Display:** A 🔵 **"CNS Penetrant Alert"** is triggered if the predicted LogBB value is 0 or higher.

---

## 4. Visualizing Permeability: The "Neuro-Active Dashboard"

The UI features a **"BBB Penetration Table"** where:

*   **Logic:** Automatic color-coding based on the LogBB value.
*   **Result:** A chemist can see at a glance if their lead is "BBB Penetrant" or "Non-Penetrant."
*   **Actionable Insight:** If a molecule is "Non-Penetrant" but intended for CNS, the system suggests the **"Bioisostere Hopper"** to reduce TPSA without losing potency.

---

## 5. Significance in CNS-Targeted Drug Development

A **Non-Penetrant** lead is rarely progressed to CNS clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **BBB-DB** datasets to provide quantitative brain concentrations ($ng/mL$) for different brain regions (e.g., Cortex vs. Hippocampus).
