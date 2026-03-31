# ⬡ ChemoFilter: Volume of Distribution ($V_d$) Logic

**Predicting Tissue Distribution and Plasma Protein Binding (PPB)**  
*Understanding Tier 7 (Celestial Engine) Pharmacokinetic Logic*

---

## 1. Executive Overview

**Volume of Distribution ($V_d$)** is the theoretical volume in which a drug is distributed. It is not a physical volume but a ratio of the dose to the final plasma concentration ($V_d = Dose / C_p$).

*   **Low $V_d$ (e.g., $< 5.0 L$):** Drug is confined to the plasma (blood).
*   **High $V_d$ (e.g., $> 1,000 L$):** Drug is widely distributed in tissues (fat, muscles).

**ChemoFilter** uses LogP and Ionization flags in Tier 7 to predict the **Fraction Unbound in Plasma ($f_u$)** and the resulting $V_d$.

---

## 2. Predicting Plasma Protein Binding (PPB)

The most common binder in blood is **Albumin**. Acidic molecules (High LogP) bind strongly to Albumin, reducing their free concentration and resulting in a **Low $V_d$**.

*   **Logic:** High LogP ($>4$) AND Acidic ($pKa < 5$) = **High PPB Flag**.
*   **Interpretation:** A lead with High PPB may have a long half-life but slow onset and require high doses to reach therapeutic concentrations.

---

## 3. Predicted $V_d$ Categories

The **"Analytical Interface Suite"** in `app.py` classifies leads into three $V_d$ bins:

| Category | Predicted $V_d$ ($L/kg$) | Scientific Interpretation |
| :--- | :--- | :--- |
| **Confined** | $< 1.0$ | Primarily in blood/interstitial fluid. |
| **Distributed** | $1.0$ to $5.0$ | Good coverage of organ systems. |
| **Tissue-Bound** | $> 10.0$ | High affinity for fat/tissues (e.g., Amiodarone). |

---

## 4. Significance in CNS Drugs

For drugs targeting the brain (CNS), a **Moderate-to-High $V_d$** and a **TPSA < 90 Å²** are required. ChemoFilter cross-references these in the **"BOILED-Egg"** model to identify potential neuro-active leads.

---

## 5. Visualizing Vd: The "Tissue Affinity" 3D Map

The **3D Conformational Force-Field Explorer** includes a **"Lipophilic Halo"** toggle where:

*   **Green Halo:** Indicates regions of high lipophilicity likely to bind to fatty tissues.
*   **Significance:** Instant visualization of potential off-target tissue accumulation liabilities.

---

## 6. How to Extend This Engine

Phase 4 (Roadmap) includes a **Full $V_d$ Regression Model** trained on 1,500 clinical pharmacokinetics trials, allowing Tier 11 to provide quantitative $V_d$ values ($L/kg$) for specific human patient weights.
