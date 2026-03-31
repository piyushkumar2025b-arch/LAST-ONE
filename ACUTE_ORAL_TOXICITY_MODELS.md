# ⬡ ChemoFilter: Acute Oral Toxicity (LD50) Models

**Predicting the $LD_{50}$ and GHS Toxicity Categories via 2D Descriptors**  
*The Safety Engineering of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

**Acute Oral Toxicity** is a critical safety metric that predicts the lethal dose ($LD_{50}$) of a compound in a single exposure. **ChemoFilter** uses structural fingerprints and local regression models to estimate the acute toxicity class, mapping results to the Global Harmonized System (GHS).

---

## 2. Defining $LD_{50}$ and GHS Categories

ChemoFilter classifies leads into one of five **GHS Toxicity Categories** based on predicted $LD_{50}$ values ($mg/kg$):

| Category | $LD_{50}$ Range ($mg/kg$) | Interpretation |
| :--- | :--- | :--- |
| **Category 1** | $\leq 5$ | **Fatal** (Extremely Toxic). |
| **Category 2** | $5$ to $50$ | **Fatal** (Highly Toxic). |
| **Category 3** | $50$ to $300$ | **Toxic** (Dangerous). |
| **Category 4** | $300$ to $2,000$ | **Harmful** (Modest Risk). |
| **Category 5** | $> 2,000$ | **Safe** (Low Acute Toxicity). |

---

## 3. The 3-Step Toxicity Prediction Sequence

When a lead enters Tier 7 (**Celestial Engine**):

1.  **Structure-Activity Mapping:** The system extracts the **Morgan Fingerprint** and identifies known "Toxophores" (e.g., specific alkylating agents).
2.  **Regression Analysis:** Calculation of the $pLD_{50}$ using a multi-linear model trained on the **Tox21** database.
3.  **Result Display:** A 🔴 **"GHS Category 2 Warning"** is triggered if the predicted $LD_{50}$ is under $50 mg/kg$.

---

## 4. Visualizing Hazard: The "GHS Dashboard"

The UI features a **"Toxicity Hazard Table"** where:

*   **Logic:** Automatic color-coding based on the GHS category.
*   **Result:** A chemist can see at a glance if their lead is "Harmful" or "Safe" for initial handled synthesis.
*   **Actionable Insight:** If a molecule is "Category 1," the system suggests the **"Scaffold Morph"** module to mitigate the toxicophores.

---

## 5. Significance in Regulatory Submission (IND)

A **GHS Category 1/2** lead is rarely progressed to Phase I clinical trials without substantial modification. ChemoFilter enables the "Early Fail" of these high-risk candidates, saving months of lab-animal validation work.

---

## 6. How to Extend This Engine

Phase 5 Roadmap involves a **Deep Learning GNN (Graph Neural Network)** trained on the **OECD (Organisation for Economic Co-operation and Development)** datasets to provide quantitative $LD_{50}$ values for different organ systems (e.g., Hepatic vs. Renal LD50).
