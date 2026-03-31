# ⬡ ChemoFilter: System Changelog

All notable changes to the engine are documented in this file. Format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

### [Unreleased]
*   **[Core Engine]** Integration of `cuGraph` via PyTorch for tensor-accelerated message passing.
*   **[Metrics]** Density Functional Theory orbital mapping natively via `Psi4` sub-process polling.

### [1M] - Omnipotent Engine Release
*   **[UI]** Added `"🚀 Demo Mode"` on the landing page for instantaneous VIT showcase initialisation, pumping 5 canonical drugs instantly into RAM.
*   **[Core]** Migrated system from basic `pandas` concatenation to `fastparquet` $O(1)$ memory mapping with JSONL Write-Ahead Log recovery for crash persistence.
*   **[Chemistry]** Upgraded the `chemo_scoring.py` heuristic module from 15 variables to over **50+ features**, including Synthesis Accessibility penalties (SA_Score) and hERG toxicophore pattern identification.
*   **[Security]** Implemented a cryptographic `SHA-256` cache interception layer inside `api_manager.py` ensuring redundant Anthropic API calls are aborted, saving bandwidth and preventing HTTP 429 API-ban cascades.
*   **[Visuals]** Built the **Crystalline Obsidian** CSS design token system, overriding Streamlit’s native blocking loading spinners with non-blocking infinite pulse animation skeletons.
*   **[Science]** Added the **BOILED-EGG Gastrointestinal Mapping** plotly plot for spatial analysis of topological surface area.

### [0.8.0] - Alpha Prototyping
*   **[Core]** Base application developed in Streamlit using strictly `RDKit`.
*   **[Chemistry]** Only base Lipinski Rule of 5 constraints were analysed. No advanced toxicity profiling or AI integration.

### [0.1.0] - Initial Commit
*   Initial Python scripts checking atomic mass constraints of simple string formulations locally.
