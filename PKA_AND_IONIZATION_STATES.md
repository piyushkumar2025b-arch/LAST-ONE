# ⬡ ChemoFilter: pKa & Ionization States

**Predicting Molecular Charge at Physiological pH (7.4)**  
*Understanding Tier 7 (Celestial Engine) Ionization Logic*

---

## 1. Executive Overview

A molecule's **pKa** (Acid Dissociation Constant) determines its **Ionization State** (Neutral vs. Charged) at a given pH. This affects membrane permeability (Neutral is better for diffusion) and receptor binding (Charged is often better for ionic anchors).

**ChemoFilter** uses a fragments-based empirical model in Tier 7 to predict the dominant charge state at physiological pH (7.4).

---

## 2. Ionized vs. Neutral Diffusion

*   **Lipophilic Neutral:** LogP is calculated for the neutral form.
*   **LogD (Lipophilicity at pH 7.4):** ChemoFilter's Tier 7 estimates the distribution coefficient ($log D_{7.4}$) to account for ionization.

$$LogD_{7.4} = \text{LogP} - \log(1 + 10^{pH - pKa}) \quad \text{(For Acids)}$$
$$LogD_{7.4} = \text{LogP} - \log(1 + 10^{pKa - pH}) \quad \text{(For Bases)}$$

---

## 3. Dominant State Categorization

The UI's **"Physicochemical Constraint Laboratory"** tab classifies molecules based on their dominant state at pH 7.4:

| State | Ionization Flag | Significance |
| :--- | :--- | :--- |
| **Neutral** | 🟡 Neutral | Most likely to cross the Blood-Brain Barrier (BBB). |
| **Basic** | 🔵 Cationic | High affinity for GPCR targets. |
| **Acidic** | 🔴 Anionic | High plasma protein binding risk ($Vd$ impact). |
| **Zwitterionic** | 🟢 Zwitterionic | Examples: Amino acids. Complex permeability profile. |

---

## 4. Predicting pKa (RDKit SMARTS)

ChemoFilter identifies ionizable groups via local SMARTS patterns:

*   **Strong Acid:** Carboxylic Acids, Sulfonic Acids.
*   **Strong Base:** Primary/Secondary Amines, Guanidines.
*   **Amphoteric:** Imidazoles, Amino acids.

---

## 5. Visualizing Charge: The "Charge Density" 3D Map

The **3D Conformational Force-Field Explorer** tab includes a **"Charge Map"** toggle where:

*   **Red Polarity:** Indicates negative/acidic regions.
*   **Blue Polarity:** Indicates positive/basic regions.
*   **Value:** Instant visualization of potential ionic anchors in a receptor pocket.

---

## 6. How to Extend This Engine

Phase 4 (Roadmap) includes a **Full pKa Graph Predictor** trained on 50,000 experimental pKa values, allowing Tier 11 to provide quantitative $pKa_1$ and $pKa_2$ indices.
