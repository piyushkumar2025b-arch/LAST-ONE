# ⬡ ChemoFilter: Plasma Protein Binding (PPB) Models

**Predicting the Fraction Unbound ($f_u$) in Blood Plasma**  
*The Pharmacokinetic Gateway of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

**Plasma Protein Binding (PPB)** is the critical factor for drug distribution. Most drugs bind to Albumin, and only the "Unbound" fraction ($f_u$) is biologically active. **ChemoFilter** uses structural fingerprints and logP/charge correlations to predict the fraction unbound ($f_u$).

---

## 2. Defining Binding Categories

ChemoFilter classifies leads into one of three **Binding Categories** based on predicted $f_u$ values ($wt\%$):

| Category | $f_u$ Range ($wt\%$) | Interpretation |
| :--- | :--- | :--- |
| **Active** | $> 20$ | **High Free Fraction.** Ideal for potency. |
| **Moderate** | $5$ to $20$ | **Moderate Binding.** Potential risk. |
| **Highly Bound** | $\leq 5$ | **Highly Bound.** Low available potency. |

---

## 3. The 3-Step PPB Prediction Sequence

When a lead enters Tier 7 (**Celestial Engine**):

1.  **Structure-Activity Correlation:** The system extracts the **LogP** and the molecule's charge at pH 7.4.
2.  **Regression Analysis:** Calculation of the $f_u$ value using a multi-linear model trained on the **PPB-DB** database.
3.  **Result Display:** A 🟠 **"Highly Bound Warning"** is triggered if the predicted $f_u$ value is 5 or lower.

---

## 4. Visualizing Distribution: The "Plasma Fate Dashboard"

The UI features a **"Plasma Protein Binding Table"** where:

*   **Logic:** Automatic color-coding based on the $f_u$ value.
*   **Result:** A chemist can see at a glance if their lead is "Active," "Moderate," or "Highly Bound."
*   **Actionable Insight:** If a molecule is "Highly Bound" but requires high potency, the system suggests the **"Bioisostere Hopper"** to reduce LogP without losing potency.

---

## 5. Significance in Pharmacokinetic Development

A **Highly Bound** lead is rarely progressed to clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **ChEMBL** datasets to provide quantitative protein-specific binding constants ($K_d$) for different plasma proteins (e.g., Albumin vs. AGP).
