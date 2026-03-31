# ⬡ ChemoFilter: Presentation Q&A / Scripted Responses

**Predicting Judge Critiques and Scientific Inquiries**  
*The "Crystalline Obsidian" Response Protocol for VIT MDP 2026*

---

## 1. Executive Overview

A high-impact demo is only half the battle. This document provides a series of **Question-and-Answer (Q&A)** scripts to prepare the team for the unpredictable inquiries of the judging panel.

---

## 2. Topic 1: Cheminformatics & Math

**Q1: "How do you calculate LogP from a 1D SMILES string?"**
*   **Response:** "We use the **Wildman-Crippen (WLOGP)** atom-typing fragmental model via the RDKit C++ kernel. It estimates the hydrophobicity by summing the contribution of each atom and its surrounding environment, which matches established pharmaceutical benchmarks." 

**Q2: "What is the significance of the SA_Score (Synthetic Accessibility)?"**
*   **Response:** "Generating a molecule on paper is easy; synthesizing it in a lab is hard. Our **SA_Score** analyzes fragment complexity and stereocenters to penalize impossible structures, ensuring that every lead identified is actually 'Druggable' in a physical laboratory."

---

## 3. Topic 2: Engineering & Data

**Q1: "How does the app handle 10,000+ compounds with sub-150MB RAM?"**
*   **Response:** "We have transitioned from row-based Pandas to **Columnar FastParquet storage**. The UI only loads the metadata and the 12 active columns (LogP, TPSA, etc.) into RAM, resulting in $O(1)$ memory scaling at any dataset size." 

**Q2: "How do you ensure data integrity if the app crashes during screening?"**
*   **Response:** "ChemoFilter implements a **Write-Ahead Logging (WAL)** system. Every molecule's state is recorded as an immutable JSONL object *before* being committed to the Parquet binary, allowing for 0% data loss across restarts."

---

## 4. Topic 3: AI & Ethics

**Q1: "Can we trust the AI Rationale? What if it hallucinates?"**
*   **Response:** "We use a **Numerical Anchor (AHMP) Protocol**. The AI is strictly restricted to interpreting the raw numerical indices (MW, LogP, hERG) provided by the RDKit engine. If the AI suggests a conclusion that conflicts with the mathematical score, the system flags a **'Scientific Conflict Detected'** alert."

**Q2: "Are you sending proprietary SMILES structures to a third-party AI?"**
*   **Response:** "No. To maintain **Structural IP**, we only send a sanitized numerical matrix (Indices without the SMILES or Name) to the AI. This protects the exact geometry of the drug while still leveraging the LLM's analytical capacity."

---

## 5. Topic 4: Commercial & Future

**Q1: "How do you compete with $100k suites like Schrodinger?"**
*   **Response:** "We offer a **Lower Barrier to Entry.** A scientist with zero coding knowledge can triage their own leads in 3 minutes. Our 'Crystalline Obsidian' UI and 'Local-First' privacy model provide the professional capability needed for startups and university labs at a fraction of the cost."

**Q2: "What is the next major step after MDP 2026?"**
*   **Response:** "We plan to integrate **Tier 11 (Metabolic Pathways)** and **Quantum DFT (Psi4)** to move from 'Drug-Likeness' to 'Biological Specificity,' enabling institutional-grade drug discovery post-showcase."
