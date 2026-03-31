# ⬡ ChemoFilter: Advanced Repository Blueprint

The ChemoFilter repository consists of approximately ~40 interdependent Python micro-modules. This modular architecture was explicitly engineered to ensure deterministic fault isolation, facilitate progressive pipeline loading, and strictly decouple UI/UX rendering vectors from extremely volatile mathematical computation mechanics.

Here is the master structural taxonomy of the active `LAST ONE/` deployment layer.

---

### 🎛️ Layer 1: Core Routing & User Interface Orchestration
*Files dictating initial layout matrices, web-server sequence handling, and aesthetic logic.*

| File Name | Primary Function |
| :--- | :--- |
| `app.py` | The definitive execution nexus. Controls Streamlit initialization, orchestrates `session_state`, coordinates the ~40 analytical tab routing sequence, and features the **Final Conclusion** summary automation logic. |
| `dashboard.py` | Renders the persistent analytical sidebars, compound search functionality overlays, and performance debug panels. |
| `landing.py` | Controls the initial "Zero-Auth" launch gate. Executes visually complex CSS animations and safely holds the user before committing heavy RDKit backend memory. |
| `landing_enhancements.py` | Powers the 10 interactive elements on the landing page, handling the event routing for exactly triggering the **`🚀 Demo Mode`**. |
| `ui_upgrade.py` | The master CSS registry establishing **Crystalline Obsidian**. Implements the dynamic `inject_ui()` to reskin Streamlit and executes non-blocking `Skeleton Loaders` prior to data fulfillment. |
| `chemo_ui_components.py` | Library of reusable localized display fragments (e.g., Risk Assessment Pills, Lead Score hex-badges, Dynamic Progress Bars). |

### 🧪 Layer 2: Pipeline Data Engineering & Terminology
*Files governing localized caching, high-performance data reading/writing, and semantic translation.*

| File Name | Primary Function |
| :--- | :--- |
| `data_engine.py` | Base analytical spine. Powers the proprietary Parquet Append functionality, JSONL Write-Ahead Logging (WAL), and handles safe `fastparquet` recovery. Radically mitigates O(N²) quadratic scaling limitations present in vanilla `pandas`. |
| `chemo_io.py` | Specialized input/output formatting utility routing SMILES blocks into Pandas dataframes. |
| `terminology.py` | Houses the `SCIENTIFIC_REGISTRY`. An abstraction dictionary translating arbitrary programmatic metrics (`hba`, `rotbonds`, `cns_mpo`) into standardized, human-readable literature strings and active tooltips. |

### ⚙️ Layer 3: Rule Logic, Heuristics & Scoring Mechanics
*Files computing qualitative pass/fail thresholds and defining custom indices.*

| File Name | Primary Function |
| :--- | :--- |
| `chemo_filters.py` | Runs exhaustive hard-limit conditionals verifying Lipinski, Veber, Ghose, Muegge, and Egan heuristics contemporaneously. |
| `chemo_scoring.py` | Calculates continuous quantitative penalties based on toxicophore structures and extracts the 0-100 proprietary `Lead_Score`. |
| `chemical_intelligence_db.py` | A localized, immutable offline database providing ultra-fast $O(1)$ lookups for >200 FDA-approved benchmark compounds (e.g., Aspirin, Metformin) to act as static baselines. |
| `scaffold_hopper.py` | Substructure generation file that recursively rips explicit side-chains off molecules to reveal core Murcko topologies. |

### 🔌 Layer 4: Network Resilience & REST API Interfaces
*Files handling external bandwidth, cryptographic payload caching, and secure data scraping.*

| File Name | Primary Function |
| :--- | :--- |
| `api_manager.py` | The primary Network Abstraction class. Intercepts all outgoing traffic to enforce SHA-256 caching deduplication and applies localized Jittered Exponential Backoff models to prevent crashing during HTTP 429 codes. |
| `api_reliability.py` | Extension class mapping exact fallback parameters and circuit-breaker configurations if an endpoint goes fully offline. |
| `api_integrations.py` | Specialized JSON scraping logic specifically querying the ChEMBL, PubChem, and PDB network endpoints. |
| `ai_explainer_tab.py` | Assembles context-heavy prompt sequences (`GEMINI_MASTER_PROMPT.md`) specifically targeted to the Anthropic API to automate complex pharmacological narrative formulation. |

### 🧮 Layer 5: The Tiered Computation Engine Stack `*_v*.py`
*The progressive execution core. Computation is broken strictly into scaling fragments ensuring the main UI continues rendering before massive processing loads finalize.*

| File Name | Primary Function |
| :--- | :--- |
| `features_v15.py` | Tier 1: Extract, Transform, Load (ETL) mapping essential physical properties (HBD, HBA, LogP, MW, Aromatic Proportions). |
| `mega_features_v20.py` | Tier 2: QED formulation arrays, explicit topological mapping, and continuous alarm parsing. |
| `hyper_zenith_v50.py` | Tier 3: Secondary lipophilicity, LogD estimates, and foundational membrane permeations (Caco-2 analogs). |
| `omnipotent_engine_v200.py` | Tier 4: Calculates extensive elemental fractions and synthetic accessibility (SA) scoring penalties. |
| `universal_analysis_v500.py` | Tier 5: Runs complex multi-dimensional descriptors and generates comprehensive toxicity profiles. |
| `celestial_engine_v1000.py` | Tier 7: Hypothetical structural mechanism evaluation matrices. |
| `omega_engine_v2000.py` & `xenon_engine_v5000.py` | Tiers 8, 9: Simulates continuous topological branching networks and intensive combinatorial evaluations. |
| `aether_engine_v10000.py` | Tier 10: "God-Mode" theoretical endpoint predicting absolute massive-scale nanotoxicity and extreme combinatorial parameters mapped onto Parquet. |
