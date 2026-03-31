# ⬡ ChemoFilter: Receptor Specificity & Target Mapping

**The Theoretical Framework of "Pharmacophore Fingerprinting"**  
*Predicting Target Classes (GPCRs, Ion Channels, Kinases) from 2D SMILES*

---

## 1. Executive Overview

Beyond physical properties (ADMET), a successful drug must be **specific**. A "Promiscuous" drug that binds to dozens of receptors (like certain antipsychotics) often causes severe side effects. **Receptor Mapping** (Tier 9: Aether Engine) uses structural fingerprints to predict the likely target classes of a compound.

---

## 2. Predicting Target Classes (Fingerprint Analysis)

ChemoFilter does not run a full docking simulation (unless the external `AutoDock Vina` wrapper is active). Instead, it uses **Morgan Fingerprint (Radius 2)** similarity matching against three curated target classes:

### A. GPCRs (G-Protein Coupled Receptors)
*   **Significance:** ~30% of all FDA-approved drugs follow this target class.
*   **Fingerprint Logic:** ChemoFilter looks for aromatic clusters, basic nitrogens, and carboxylic acid anchors characteristic of the **Amine GPCR** family (e.g., Dopamine, Serotonin).

### B. Kinases (ATP-Binding Competitors)
*   **Significance:** Crucial for oncology (cancer) therapeutics.
*   **Fingerprint Logic:** Identification of **H-Bond Donor-Acceptor-Donor (D-A-D)** patterns that mimic the adenine ring of ATP.

### C. Ion Channels
*   **Significance:** Critical for CNS and cardiac drugs.
*   **Fingerprint Logic:** High LogP and basic centers (tertiary amines) are often flags for **hERG** or **Na+ Channel** activity.

---

## 3. Promiscuity Assessment (Frequent Hitters)

The **"Mechanistic Rationale" (Anthropic AI Interpreter)** flag identifies "Pan-Assay Interference Compounds" (PAINS), but also goes further by identifying "Frequent Hitters"—molecules that appear as leads in many different assays but have no specific target.

| Flag | Metric | Interpretation |
| :--- | :--- | :--- |
| **Specific Lead** | High Similarity to one target class. | Potential for a high-potency drug with low side effects. |
| **Poly-Pharmacology** | High Similarity to multiple target classes (e.g., Kinases + GPCRs). | Potential for a complex drug (e.g., multi-targeted kinase inhibitors). |
| **Non-Specific Binder** | No similarity to any known target classes. | High risk of off-target toxicity. |

---

## 4. Visualizing Specificity: The "Target Web"

The UI features a **Radar Chart (Target Web)** mapping the probability of binding across 12 biological classes.

*   **Logic:** A sharp, focused "spike" on the radar chart is ideal.
*   **Result:** A chemist can see at a glance if their "Kinase Lead" is accidentally looking like a "Dopamine Antagonist."

---

## 5. Future Roadmap: The "Air-Gapped" Docking Suite

Phase 6 aims to integrate a fully local **AlphaFold-2 / autodock-vina** pipeline that can run 3D docking without any external web access, allowing Tier 9 to provide exact $kcal/mol$ binding energy values for user-uploaded Protein Data Bank (.pdb) structures.
