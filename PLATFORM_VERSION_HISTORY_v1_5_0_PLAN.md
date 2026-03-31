# ⬡ ChemoFilter: Platform Version History (v1.5.0 Roadmap)

**Transitioning from "Showcase Snapshot" to "Institutional Suite"**  
*The Technical Roadmap for Q3 2026+ post-MDP 2026*

---

## 1. Executive Overview

This version (v1.5.0) represents the **"Institutional Edition"** of ChemoFilter. It is the first major update planned after the **VIT MDP 2026** presentation, focusing on **Group Collaboration**, **Quantum Accuracy**, and **Systems Biology**.

---

## 2. Release Notes: ChemoFilter v1.5.0 (Projected)

### **I. Major Features (The "Group Core")**
*   **Collaborative Vaults:** Multiple scientists working on a shared `compounds.parquet` via Git-LFS or a centralized S3 Bucket.
*   **Audit Logging (21 CFR Part 11):** Electronic signatures and SHA-256 structural audit trails for regulatory compliance.
*   **Distributed Dask Cluster:** Offloading Tier 7-9 calculations to a multi-node institutional cluster.

### **II. Advanced Research Modules**
*   **Tier 11 (Metabolic Pathways):** Integrating results with the **KEGG** and **Reactome** metabolic cycles.
*   **Quantum DFT Integration:** Using **Psi4** and **PySCF** for extreme HOMO/LUMO band-gap precision.
*   **SMILES-to-SMILES LSTM:** A generative model (Phase 5) that can "Grow" a lead from a fragment autonomously while maintaining target specificity.

---

## 3. Version Progression (The Development Cycle)

| Version | Date | Status | Major Milestone |
| :--- | :--- | :--- | :--- |
| **v1.0.0** | APR 2026 | **Current** | Official **MDP 2026 Showcase Edition.** |
| **v1.2.0** | JUN 2026 | Planning | Initial **Dask Cluster** prototype. |
| **v1.5.0** | OCT 2026 | Projected | Full **Institutional Suite** launch. |

---

## 4. Known Features in Development (v2.0.0 Vision)

1.  **Mobile PWA Wrapper:** Viewing research results on a smartphone.
2.  **Air-Gapped Local LLMs (Llama-3):** Removing the need for an external API key for AI interpretations.
3.  **Federated Bioisostere Library:** Institutional users uploading their own successful lab bioisosteres.

---

## 5. Credits & Institutional Partnerships

*   **Principal Engineer:** [Student Name]
*   **Institutional Partners:** VIT Chennai (Department of Computational Biology / Computer Science).

---

## 6. Stability & Bug Reporting

ChemoFilter v1.5.0 is thoroughly tested on **Windows/WSL2/macOS**. Any architectural issues identified during the institutional pilot should be logged in the **"Development Tracker"** on GitHub.
