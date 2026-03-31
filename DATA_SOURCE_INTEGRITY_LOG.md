# ⬡ ChemoFilter: Data Source Integrity & Versioning Log

**Standardization of Databases and Experimental Constants**  
*Curated Libraries Used by the 9-Tier Processing Engine*

---

## 1. Executive Overview

ChemoFilter's "Vanguard" and "Aether" engines are only as reliable as the data used for their training and benchmarking. This log documents the specific versions and provenance of the scientific databases integrated into the project.

---

## 2. Core Cheminformatics Libraries

| Library | Version | Role | Repository Source |
| :--- | :--- | :--- | :--- |
| **RDKit** | 2024.03.1 | Core kernel for all 2D/3D descriptor math. | conda-forge / rdkit |
| **PubChem REST API** | v2.1 | Fetches canonical SMILES, CIDs, and metadata. | NIH / NCBI |
| **ChEMBL** | v34 | Source for pIC50 and inhibition baselines. | EMBL-EBI |
| **PDB (Protein Data Bank)** | 2026 Snapshot | Coordinates for receptor specificities. | RCSB |

---

## 3. Benchmarking Datasets (Internal Reference)

ChemoFilter includes a curate `chemical_intelligence_db.py` of 200+ FDA-approved drugs for statistical normalization.

*   **Lipinski Ro5 Baseline:** Derived from the **ZINC15** "drug-like" subset (1.2M compounds).
*   **Aqueous Solubility (logS):** Based on the **Delaney Set (ESOL)** of 1,144 unique compounds.
*   **PAINS Filters:** Hard-coded SMARTS patterns from the **Baell & Holloway (2010)** publication.

---

## 4. Physicochemical Constants Logic

ChemoFilter uses standardized atomic weights and electronegativity values derived from:

*   **Atomic Weights:** IUPAC (2025) standard atomic weights.
*   **LogP Calculations:** Wildman-Crippen (WLOGP) atom-typing methodology.
*   **Force-Field:** Merck Molecular Force Field (**MMFF94**) for energy minimization.

---

## 5. Security & Validity Hashes

To ensure the local parquet database (`data/compounds.parquet`) hasn't been corrupted or altered:

1.  **MD5 Checksum:** A checksum is calculated every 1,000 writes.
2.  **Schema Enforcement:** The `data_engine.py` restricts new column additions to only those authorized in the `engine_orchestrator.py` registry.

---

## 6. Future: Federated Cheminformatics

Phase 4 Roadmap includes the **Federated Query Engine**, which will allow ChemoFilter to cross-reference hits against internal lab data (hosted as private Parquet files) alongside public data from the NIH and EBI.
