# ⬡ ChemoFilter: Carcinogenicity & Chronic Toxicity Roadmap

**Predicting Long-Term Health Risks and Potential Carcinogens**  
*The High-Resolution Chronic Hazard Gateway of Tier 9 (Aether Engine)*

---

## 1. Executive Overview

**Carcinogenicity** is the potential for a compound to cause cancer. **ChemoFilter** uses structural fingerprints and chronic toxicity alerts to predict the carcinogenic potential, mapping results to the CPDB (Carcinogenic Potency Database).

---

## 2. Defining Carcinogenicity Categories

ChemoFilter classifies leads into one of two **Carcinogenicity Categories** based on predicted TD50 values ($mg/kg/day$):

| Category | TD50 Range | Interpretation |
| :--- | :--- | :--- |
| **High** | $\leq 10$ | **High Carcinogenic Risk.** Potential human carcinogen. |
| **Moderate** | $10$ to $100$ | **Possible Carcinogen.** Potential risk. |
| **Non** | $> 100$ | **Non-Carcinogenic.** Safe for initial research. |

---

## 3. The 3-Step Carcinogenicity Prediction Sequence

When a lead enters Tier 9 (**Aether Engine**):

1.  **Structure-Activity Mapping:** The system extracts the **Morgan Fingerprint** and identifies known "Chronic Toxicity Alerts" (e.g., specific alkylating agents).
2.  **Regression Analysis:** Calculation of the TD50 value using a multi-linear model trained on the **CPDB** database.
3.  **Result Display:** A 🔴 **"High Carcinogenicity Warning"** is triggered if the predicted TD50 value is under 10.

---

## 4. Visualizing Hazard: The "Chronic Toxicity Dashboard"

The UI features a **"Carcinogenicity Hazard Table"** where:

*   **Logic:** Automatic color-coding based on the carcinogenicity category.
*   **Result:** A chemist can see at a glance if their lead is "High," "Moderate," or "Non" carcinogen.
*   **Actionable Insight:** If a molecule is a "High Carcinogen," the system suggests the **"Scaffold Morph"** module to mitigate the structural alerts.

---

## 5. Significance in Long-Term Drug Development

A **High Carcinogenic** lead is rarely progressed to long-term clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **ToxHub** datasets to provide quantitative carcinogenic probabilities for different organ systems (e.g., Hepatic vs. Renal).
