# ⬡ ChemoFilter: Gastrointestinal Absorption (HIA) Models

**Predicting Oral Bioavailability and GI Permeability**  
*The Oral Delivery Gateway of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

**Gastrointestinal Absorption (HIA)** is the critical factor for orally administered drugs. **ChemoFilter** uses structural fingerprints and logP/TPSA correlations to predict the percentage of the drug absorbed ($wt\%$).

---

## 2. Defining Absorption Categories

ChemoFilter classifies leads into one of three **Absorption Categories** based on predicted HIA values ($wt\%$):

| Category | HIA Range ($wt\%$) | Interpretation |
| :--- | :--- | :--- |
| **High** | $\geq 80$ | **Excellent Absorption.** Ideal for oral drug. |
| **Moderate** | $20$ to $80$ | **Moderate Absorption.** Potential risk. |
| **Low** | $< 20$ | **Poorly Absorbed.** Non-oral drug only. |

---

## 3. The 3-Step Absorption Prediction Sequence

When a lead enters Tier 7 (**Celestial Engine**):

1.  **Structure-Activity Correlation:** The system extracts the **LogP** and **TPSA** (Topological Polar Surface Area).
2.  **Regression Analysis:** Calculation of the HIA value using a multi-linear model trained on the **HIA-DB** database.
3.  **Result Display:** A 🟢 **"High Absorption Alert"** is triggered if the predicted HIA value is 80 or higher.

---

## 4. Visualizing Oral Delivery: The "GI Permeability Dashboard"

The UI features a **"Gastrointestinal Absorption Table"** where:

*   **Logic:** Automatic color-coding based on the HIA value.
*   **Result:** A chemist can see at a glance if their lead is "High," "Moderate," or "Low" absorption.
*   **Actionable Insight:** If a molecule is "Poorly Absorbed" but intended for oral, the system suggests the **"Bioisostere Hopper"** to reduce TPSA without losing potency.

---

## 5. Significance in Oral-Targeted Drug Development

A **Poorly Absorbed** lead is rarely progressed to oral clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **HIA-DB** datasets to provide quantitative absorption concentrations ($ng/mL$) for different organ systems (e.g., Stomach vs. Intestine).
