# ⬡ ChemoFilter: Scaffold Diversity & Fragment Library Analysis

**The Engineering of a "Healthy" Drug Library**  
*Using Murcko Scaffolds to Assess Chemical Space Coverage*

---

## 1. Executive Overview

In large-scale screening, it is more important to have 10 compounds from different **Scaffold Families** than 100 compounds of the same type. **Scaffold Diversity** refers to the variety of ring systems and frameworks in a chemical library. ChemoFilter helps users identify if their research is "Diverse" or if it is redundantly focused on a single structural motif.

---

## 2. Murcko Scaffold Extraction (RDKit)

The system uses the `MurckoScaffold.GetScaffoldForMol` function to identify the core framework of every molecule.

1.  **De-Sidechaining:** Ripping off all non-ring substituents (e.g., methyls, halogens).
2.  **Ring-Bridge System:** Only the rings and the linkers between them remain.
3.  **Result:** The **Canonical Scaffold**. 

---

## 3. The Scaffold Diversity Index ($I_s$)

ChemoFilter calculates a **Diversity Index** for any given library of leads ($N$):

$$I_s = \frac{N_{scaffolds}}{N_{compounds}} \times 100 \%$$

*   **High Diversity ($I_s > 80 \%$):** A broad exploration of chemical space.
*   **Low Diversity ($I_s < 20 \%$):** A focused library, likely exploring a single SAR (Structure-Activity Relationship) around a known lead.

---

## 4. Visualizing Fragments: The "Sunburst" Chart

The UI features a **Sunburst Chart** where the inner ring represents the core ring systems and the outer ring shows the specific side-chain modifications.

*   **Scientific Value:** This chart instantly shows if a user's library is "Diverse" or if it is redundant.
*   **Actionable Insight:** If 80% of your leads share a **Benzene core**, the system will flag the library as "Low Scaffold Diversity" and suggest trying alternative **Morphs** (see `BIOIS_MORPHING_ALGORITHM.md`).

---

## 5. RECAP Fragment Analysis

ChemoFilter identifies possible synthetic origins using the **RECAP (Retrosynthetic Combinatorial Analysis Procedure)** methodology:

*   **Logic:** How many steps would it take to synthesize the core?
*   **SA_Score Impact:** Molecules with common, proven scaffolds (like indoles) receive a **Synthetic Accessibility (SA)** bonus, while rare, strained ring systems receive a penalty.

---

## 6. Future: Scaffold Hopping (Phase 5)

Phase 5 aims to integrate a **SMILES-to-SMILES LSTM** that can "Hop" from one scaffold class to an entirely different one while maintaining the same pharmacophore placement.
