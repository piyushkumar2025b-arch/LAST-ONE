# ⬡ ChemoFilter: Skin Sensitization & Irritation Models

**Predicting the LLNA (Local Lymph Node Assay) Class via 2D Descriptors**  
*The Dermal Toxicology Gateway of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

**Skin Sensitization** is the potential for a compound to cause an allergic contact dermatitis response. **ChemoFilter** uses structural fingerprints and structural alerts to predict the sensitizing potential, mapping results to the LLNA (Local Lymph Node Assay).

---

## 2. Defining Sensitization Categories

ChemoFilter classifies leads into one of three **Sensitization Categories** based on predicted EC3 values ($wt\%$):

| Category | EC3 Range ($wt\%$) | Interpretation |
| :--- | :--- | :--- |
| **High** | $\leq 2.0$ | **Strong Sensitizer.** High risk of allergic response. |
| **Moderate** | $2.0$ to $10.0$ | **Moderate Sensitizer.** Potential risk. |
| **Non** | $> 10.0$ | **Non-Sensitizer.** Safe for dermal contact. |

---

## 3. The 3-Step Sensitization Prediction Sequence

When a lead enters Tier 7 (**Celestial Engine**):

1.  **Structure-Activity Mapping:** The system extracts the **Morgan Fingerprint** and identifies known "Sensitizing Alerts" (e.g., specific alkylating agents).
2.  **Regression Analysis:** Calculation of the EC3 value using a multi-linear model trained on the **LLNA** database.
3.  **Result Display:** A 🔴 **"High Sensitization Warning"** is triggered if the predicted EC3 value is under 2.0.

---

## 4. Visualizing Hazard: The "Dermal Toxicity Dashboard"

The UI features a **"Sensitization Hazard Table"** where:

*   **Logic:** Automatic color-coding based on the sensitization category.
*   **Result:** A chemist can see at a glance if their lead is "High," "Moderate," or "Non" sensitizer.
*   **Actionable Insight:** If a molecule is a "High Sensitizer," the system suggests the **"Scaffold Morph"** module to mitigate the structural alerts.

---

## 5. Significance in Cosmetic & Topical Drug Development

A **High Sensitizing** lead is rarely progressed to topical clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **OECD (Organisation for Economic Co-operation and Development)** datasets to provide quantitative EC3 values for different organ systems (e.g., Hepatic vs. Renal).
