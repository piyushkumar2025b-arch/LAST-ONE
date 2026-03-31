# ⬡ ChemoFilter: Technology Infrastructure & Resource Stack

The platform is constructed on an elite stack of open-source Python libraries, data-storage technologies, and active REST APIs. This document explicitly catalogs every external dependency utilized by `ChemoFilter`, detailing exactly *how* and *why* it was implemented.

---

## 1. Primary Presentation & UI Layer

| Technology | Purpose in ChemoFilter | Implementation Details |
| :--- | :--- | :--- |
| **Streamlit (v1.x+)** | Core Web Application Framework | Powering the entire reactive, stateless user interface. Streamlit transpiles centralized Python commands into an optimized React.js frontend dynamically. Features automatic state re-rendering upon parameter adjustment. |
| **Plotly Graph Objects** | Interactive WebGL Visualizations | Selected over standard `matplotlib` to ensure non-blocking interactivity. Renders the massive 3D Cartesian coordinates, Tanimoto PCA clusters, and radar charts. Utilizes GPU acceleration to prevent browser freezing. |
| **Crystalline Obsidian** | Custom Interface Design System | A highly bespoke, hard-coded CSS injection library designed exclusively for this application outliving standard Streamlit themes. Features neon-electric typography (`Syne` and `JetBrains Mono`), skeleton asynchronous loaders, and $z$-index floating action buttons. |

## 2. Chemical Intelligence & Processing Backbone

| Technology | Purpose in ChemoFilter | Implementation Details |
| :--- | :--- | :--- |
| **RDKit (`rdkit`)** | Industry-Standard Cheminformatics C++ Library | Powering the absolute core of the predictive engine. Generates continuous arrays mapping Lipinski, Veber, and QED constraints. Conducts deterministic substructure SMARTS matching for PAINS identifiers and extracts Morgan (ECFP4) Fingerprint tensors. |
| **FilterCatalog** | Rapid Structural Alert Queries | Utilized natively via `rdkit.Chem.FilterCatalog` to execute ultra-fast multi-threaded substructure matching against thousands of known Brenk and NIH toxicological hazard definitions simultaneously. |
| **Murcko Scaffolds** | Topological Abstraction | Used by the `scaffold_hopper.py` engine to programmatically strip side-chains and identify the base pharmacophore. Facilitates lead-optimization by locating bioisostere replacements. |

## 3. High-Performance Data Engineering

| Technology | Purpose in ChemoFilter | Implementation Details |
| :--- | :--- | :--- |
| **Pandas (`pd`)** | Tabular Data Processing | High-performance vectorized operations forming the analytical spine of the batch processing mechanics. Manages the ultimate 200+ column `display_data` matrix. |
| **FastParquet** | O(1) Memory Compression storage | Implemented to permanently strip away traditional CSV/SQLite I/O bottlenecks. Parquet structures data in columns with massive compression thresholds, yielding $O(1)$ memory overhead during thousands of rapid append operations. Located securely in `data/compounds.parquet`. |
| **JSONL WAL** | Write-Ahead Logging (Crash Safety) | A pure-Python fail-safe data recovery mechanism mirroring Enterprise Database topologies (e.g., PostgreSQL). Before memory caches flush to Parquet, atomic dictionaries are appended to `data/compounds_wal.jsonl`. |

## 4. Cloud Infrastructure & REST APIs

| External Service | Data Retrieved | Network Management Strategy |
| :--- | :--- | :--- |
| **Anthropic Claude 3 AI** | Pharmacological Translation | Deployed as an integrated "Scientific Explainer" (`ai_explainer_tab.py`). Transmits serialized QED & Lipinski dictionaries to the LLM to retrieve localized, human-readable natural language interpretations for clinical audiences. Managed via specific prompt arrays (`GEMINI_MASTER_PROMPT.md`). |
| **PubChem API (NCBI)** | Empirical Metadata & Synonyms | Hit dynamically specifically to retrieve IUPAC nomenclatures attached to unmapped SMILES strings and biological assay results. |
| **ChEMBL API (EMBL-EBI)** | Protein Target Affinities | Operates strictly via asynchronous JSON extraction. Retrieves exact macromolecular IC50 targets attached to the generated molecule frameworks. |
| **PDB (Protein Data Bank)** | Crystallographic 3D Models | Integrated for continuous visual structural queries and ligand docking representation requests. |

## 5. Network Resiliency Security Protocols

Deploying an application requiring massive continuous HTTP polling necessitates strict safety firewalls:

1.  **Jittered Exponential Backoff:** The Anthropic and PubChem APIs enforce aggressive rate limits ($x$ calls / minute). The `api_reliability.py` module wraps every single external call. If a `HTTP 429 Too Many Requests` is fired, the platform silently catches it, applies a randomized temporal delay (Jitter), and retries in the background, maintaining total application stability.
2.  **SHA-256 Payload Hashing:** All analytical requests pass through a cryptographic hash generating a unique ID based *exactly* on the text contents. The local `session_state` checks this hash. If identical requests are fired (e.g., pulling data for 'Aspirin' multiple times across tabs), it returns the memory context instantaneously instead of executing redundant bandwidth-intensive HTTPS queries.
