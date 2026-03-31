# ⬡ ChemoFilter: PAINS Alert SMARTS Pattern Registry

**Detecting Pan-Assay Interference Compounds (PAINS) via Substructure Matching**  
*The High-Throughput Screening (HTS) Gateway of Tier 1 (Vanguard Core)*

---

## 1. Executive Overview

**PAINS (Pan-Assay Interference Compounds)** are chemical motifs that frequently show activity in many different biochemical assays, not because they are potent drugs, but because they interfere with the assay's readouts (e.g., through oxidation, color, or non-specific binding). 

ChemoFilter uses the **Baell & Holloway (2010)** SMARTS pattern registry to automatically flag these "False Positive" drug signals.

---

## 2. Key PAINS Families (SMARTS Patterns)

ChemoFilter's `chemo_filters.py` iterates through 480+ SMARTS strings. Here are five of the most critical:

1.  **Quinones:** Often act as redox-cyclers, generating ROS (Reactive Oxygen Species) that interfere with metabolic assays.
2.  **Epoxides:** Highly reactive electrophiles that bind non-specifically to any protein surface.
3.  **Phenolic Mannich Bases:** Can sequester crucial metal ions needed for the protein's activity.
4.  **Toxophores:** Michael acceptors (e.g., $\alpha, \beta$-unsaturated carbonyls) that form irreversible covalent bonds.
5.  **Catechols:** Often undergo rapid oxidation to benzoquinones, giving false signals in UV-Vis based assays.

---

## 3. The PAINS "Banned List" Protocol

If a molecule contains a PAINS motif:

*   **Flag:** A 🔴 **"High Liability: PAINS Alert"** toast is triggered in `app.py`.
*   **Result:** The **Lead Score** is penalized by **10 points** to reflect the high risk of it being a "Frequent Hitter" in the wet lab.
*   **Actionable Insight:** The AI Interpreter will suggest the **"Scaffold Morph"** module to replace the offending fragment while maintaining structural integrity.

---

## 4. Why PAINS Matter in Drug Discovery

In a standard high-throughput screen, 5% to 12% of hits are PAINS. If these are not filtered computationally, they can cost a lab **months of wasted work** on synthesizing and testing molecules that have no specific target.

---

## 5. Visualizing the Hazard: The "Hazard Overlay" 3D Map

The **3D Conformational Force-Field Explorer** tab includes a **"Hazard Overlay"** where:

*   **Glowing Toxic-Orange Group:** The specific atoms in the SMILES string that match the PAINS pattern are highlighted.
*   **Value:** Instant visualization for the chemist to see exactly which fragment is the liability.

---

## 6. How to Extend This Registry

The `chemo_filters.py` module allows for the addition of custom SMARTS patterns. Scientists can "Whitelist" certain PAINS if their specific biological target (e.g., covalent inhibitors) specifically requires that reactive group.
