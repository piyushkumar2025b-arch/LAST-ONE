# ⬡ ChemoFilter: Biochemical Pathway Integration (Planned Tier 11)

**Mapping ADMET Results to Global Metabolic Pathways (KEGG, Reactome)**  
*The Transition from Structural Modeling to Systems Biology*

---

## 1. Executive Overview

ChemoFilter currently focuses on the **Pharmacokinetics (PK)** of molecules (what the body does to the drug). The next phase of development (Tier 11) will focus on **Pharmacodynamics (PD)** (what the drug does to the body) by integrating results with biochemical pathway maps.

---

## 2. Target Identification (Tier 11 Logic)

Tier 11 will use **Reverse Screening** (Inverse Docking) to identify potential protein targets for a given SMILES structure:

*   **Logic:** If a molecule's **Murcko Scaffold** is similar to a known kinase inhibitor, ChemoFilter will flag the **Map Kinase Pathway** as a potential site of action.
*   **Database Integration:** Utilizing the **KEGG (Kyoto Encyclopedia of Genes and Genomes)** REST API to cross-reference targets with biological pathways.

---

## 3. Toxicity Pathway Mapping (AOP)

Using the **Adverse Outcome Pathway (AOP)** framework, ChemoFilter will map hERG and PAINS alerts to specific cellular injuries:

*   **hERG Alert** $\rightarrow$ **K+ Channel Blockage** $\rightarrow$ **Delayed Ventricular Repolarization** $\rightarrow$ **Cardiac Arrhythmia.**
*   **CYP3A4 Inhibition** $\rightarrow$ **Altered Metabolic Clearance** $\rightarrow$ **Drug-Drug Interaction (DDI) Risk.**

---

## 4. Visualizing Pathways with WebGL

The **"Mechanistic Logic"** tab (Tier 9) is being redesigned to include an interactive **D3.js or Mermaid** diagram showing the molecule's predicted path through human metabolic cycles:

1.  **GI Absorption:** Predicted by the **BOILED-Egg** model.
2.  **Hepatic Metabolism:** Predicted by the **CYP450** isoenzyme table.
3.  **Renal Excretion:** Predicted by the **ESOL Solubility** and molecular weight ($MW$).

---

## 5. Case Study: Olanzapine Pathway Map

Olanzapine (one of our **Demo Mode** anchors) is a dopamine and serotonin antagonist. Tier 11 would automatically load the **Serotonergic Synapse** and **Dopaminergic Synapse** maps from the Reactome database to visualize its therapeutic mechanism of action.

---

## 6. Future Data Sources (Phase 4 Roadmap)

*   **ChEMBL:** To fetch experimental $IC_{50}$ and $K_i$ values for validated targets.
*   **Reactome:** To map molecular targets to hierarchical biological processes.
*   **String-DB:** To map protein-protein interaction (PPI) networks affected by the drug's primary target.
