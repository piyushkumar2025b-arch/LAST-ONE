# ⬡ ChemoFilter: Fragment-Based Drug Discovery (FBDD)

**Building Leads from Experimental Chemical Building Blocks**  
*The Science of "Growing" a Molecule via RECAP Fragment Analysis*

---

## 1. Executive Overview

Instead of screening 1,000,000 large molecules, **Fragment-Based Drug Discovery (FBDD)** screens 1,000 small "Fragments" (MW < 250). ChemoFilter supports FBDD through its **Tier 5 (Omni-Science)** engine, which identifies the potential for a small molecule to be "Grown" into a potent drug lead.

---

## 2. The "Fragment-to-Lead" Logic (The Rule of 3)

FBDD follows a more stringent version of the Rule of Five, called the **"Rule of Three" (Ro3)**:

*   **MW < 300**
*   **LogP < 3**
*   **HBD < 3**
*   **HBA < 3**

**ChemoFilter Implementation:** Tier 5 identifies if a molecule meets the Ro3 criteria. If so, it is flagged as a **"Viable Fragment Starter"** for lead optimization.

---

## 3. The RECAP (Retrosynthetic Combinatorial Analysis) Algorithm

ChemoFilter's `scaffold_hopper.py` uses the **RECAP** algorithm to "Rip" a lead apart into its component fragments:

1.  **Logic:** Identification of common synthetic bonds (e.g., Amides, Esters, Urea linkers).
2.  **Action:** The molecule is broken into Fragments A, B, and C.
3.  **Scientific Value:** The chemist can see which specific fragment is the **"Pharmacophore Anchor"** and which is the "Bloat" that needs to be replaced.

---

## 4. Visualizing Fragments: The "Sunburst" Chart

The UI features a **"Fragment-Sunburst Chart"** (Tier 5) where:

*   **Inner Ring:** Core ring systems (e.g., Pyridine, Indole).
*   **Outer Ring:** The specific side-chain additions.
*   **Significance:** Instant visualization of whether your library is exploring a single chemical space or is diverse enough for a successful FBDD campaign.

---

## 5. Growing the Lead: The "Bioisostere Hopper"

Once a "Fragment Starter" is identified, the **"Bioisostere Morph"** module suggests "Growing" the lead:

*   **Logic:** Suggesting compatible side-chains from a library of 2,000+ FDA-proven bioisosteres.
*   **Result:** A chemist can computationally "Add" a methyl or hydroxyl group to see how it improves the **Lead Score** instantly.

---

## 6. How to Extend This Module

Phase 5 (Roadmap) includes a **"Fragment-Merging Suite"**, which identifies two different fragments that bind to different parts of a receptor pocket and suggests a "SMILES Linker" string to combine them into a single, high-affinity lead.
