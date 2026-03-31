# ⬡ ChemoFilter: Metabolic Reactivity & Phase I/II Alert List

**Structural Alerts for Predicting Molecular Biotransformations**  
*The High-Resolution Toxicology Gateway of Tier 7 (Celestial Engine)*

---

## 1. Executive Overview

Metabolism is a two-phase process. **Phase I** (Functionalization) involves oxidation by CYP450. **Phase II** (Conjugation) involves adding a polar group (e.g., glucuronic acid) for excretion. **ChemoFilter** uses structural alerts to predict if a lead will be a "victim" of these metabolic pathways.

---

## 2. Phase I Alerts (Oxidative Soft Spots)

1.  **Aromatic Hydroxylation:** Unhindered phenyl rings (e.g., in benzene or polycyclic hydrocarbons).
2.  **Benzylic Oxidation:** Methyl or methylene groups attached to a phenyl ring (e.g., toluene derivatives).
3.  **N-Dealkylation:** Tertiary amines (e.g., $N,N$-dimethyl groups).
4.  **O-Dealkylation:** Methoxy groups (e.g., anisole derivatives).
5.  **S-Oxidation:** Thioethers (e.g., sulfides).

---

## 3. Phase II Alerts (Conjugation Liabilities)

1.  **Glucuronidation (UGT):** Phenols, carboxylic acids, and 1°/2° amines. 
2.  **Sulfation (SULT):** Phenols and aromatic amines.
3.  **Acetylation (NAT):** Primary amines and hydrazines.
4.  **Glutathione (GSH) Conjugation:** Michael acceptors (e.g., $\alpha, \beta$-unsaturated carbonyls) and epoxides. **(High Hazard Flag).**

---

## 4. Predicting "Toxic Metabolites"

Some molecules are not toxic themselves but become toxic after Phase I metabolism (Bioactivation).

*   **Logic:** Identification of aromatic amines ($Ar-NH_2$) which can be oxidized to reactive nitrenium ions.
*   **Result:** A **"Bioactivation Hazard"** flag in the **"Hazard Overlay Map"**. 

---

## 5. Visualizing Metabolic Fate: The "Atom-Level" Map

The **3D Conformational Force-Field Explorer** includes a **"Metabolic Fate"** toggle:

*   **Red Atom Glowing:** Indicates a site of potential Phase I oxidation.
*   **Blue Atom Glowing:** Indicates a site of potential Phase II conjugation.
*   **Value:** An instant prompt for a chemist to add a "Shield" (e.g., a Fluorine atom) or rigidify the scaffold.

---

## 6. How to Extend This Logic

Phase 5 Roadmap involves a **Metabolic Graph Predictor** that can "Generate" the likely structure of the primary metabolite, allowing Tier 9 to run a separate ADMET screen on the metabolite itself.
