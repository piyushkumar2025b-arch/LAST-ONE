# ⬡ ChemoFilter Master Documentation Portal

Welcome to the **ChemoFilter** platform directory. Due to the extreme multidisciplinary nature of this application—spanning algorithmic computer science, data engineering, physical chemistry, and clinical pharmacology—the documentation has been strictly modularized. 

Use this directory to navigate the massive suite of architectural blueprints and scientific registries prepared for the **VIT Chennai MDP 2026 Showcase**.

---

### 🏛️ 1. Project Architecture & Deployment
* **[Master Project Blueprint](project.md)**
  * *Read first.* The definitive executive summary and high-level architecture document. Explains the "Demo Mode" launch sequence, the $O(1)$ memory innovations, the 9-Tier Processing Engine, and how the platform merges 5 distinct scientific disciplines.
* **[Architecture Decision Records (ADR)](ARCHITECTURE_DECISIONS.md)**
  * Details the exact strategic trade-offs made during development (e.g., choosing `fastparquet` over `pandas`, Streamlit over React, and implementing Cryptographic API Hashing).
* **[Installation & Setup Guide](SETUP.md)**
  * Complete, step-by-step walkthrough on how to configure RDKit natively, set up the virtual Python environment locally, and securely manage API keys for the Anthropic engine.
* **[Development Roadmap](ROADMAP.md)**
  * The long-term trajectory of the platform, detailing the transition from rule-based heuristics to Graph Neural Networks (GNNs) and Quantum Mechanics calculations.

### 💻 2. Repository & Code Infrastructure
* **[Repository Code Modules](code_modules.md)**
  * A comprehensive 5-layer index breaking down all 40+ Python `.py` scripts. Maps exactly where the User Interface (`Layer 1`) separates from the mathematical engines (`Layer 5`).
* **[Technology & Resource Stack](resources.md)**
  * An exhaustive deep-dive detailing the open-source libraries (e.g., `FastParquet`, `RDKit`, `Streamlit WebGL`), and the external API databases (PubChem, ChEMBL).
* **[Data Pipeline & Parquet Routing](DATA_PIPELINE.md)**
  * Explicit technical documentation explaining the $O(1)$ memory pipeline and Write-Ahead Log cache physically solving the Pandas bottleneck.
* **[System Testing & QA](TESTING_AND_QA.md)**
  * A framework governing unit testing, regression testing on Lipinski bounds, and ensuring RDKit C++ segmentation faults are contained.
* **[System Troubleshooting](TROUBLESHOOTING.md)**
  * A guide to resolving critical errors, including out-of-memory cascades, and API network timeouts.
* **[Scale Performance & Benchmarks](PERFORMANCE_BENCHMARKS.md)**
  * Speed latency numbers explicitly validating the `O(1)` memory engine versus quadratic pandas operations.
* **[System Infrastructure Costs](INFRASTRUCTURE_COSTS.md)**
  * Hardware and cloud costing models explicitly mapped for AWS or local machine instances for processing $10,000$+ compounds.

### 🧬 3. Scientific Data & Pharmacology
* **[Comprehensive Scientific Glossary](terms.md)**
  * A massive semantic dictionary explicitly defining over 30 fundamental cheminformatic metrics. Explains the clinical ramifications of variables like *hERG Risk*, *Fsp3 Fractons*, and *Ligand Efficiency*.
* **[Peer-Reviewed Bibliography](references.md)**
  * Cites the 11 foundational pharmaceutical papers and maps exactly *which Python script* natively executes their mathematical formulas.
* **[Algorithmic & Math Theory](ALGORITHMS_AND_MATH.md)**
  * Deep-dive documentation showing the exact Euclidean math generating SA Penalties and Tanimoto intersections.
* **[Historical Clinical Trial Case Studies](CLINICAL_TRIAL_CASE_STUDIES.md)**
  * Theoretical modeling of famous clinical trial failures/successes (e.g. Vioxx, Gleevec) using ChemoFilter rules.
* **[Scientific Validation](SCIENTIFIC_VALIDATION.md)**
  * Explains how the platform's `Lead_Score` algorithm was validated against known FDA-approved drugs.
* **[Algorithmic Limitations](KNOWN_LIMITATIONS.md)**
  * Technological constraints addressing the limitations of 2D heuristics versus in-vivo 3D receptor simulations.
* **[Data Dictionary](DATA_DICTIONARY.md)**
  * Variable, type, and boundary limits exported when users save their compound datasets to `.CSV` or `.JSON`.

### 🤝 4. Community, Logistics & Project Management
* **[VIT 2026 Presentation Script](PRESENTATION_SCRIPT.md)**
  * *Crucial for the MDP Showcase.* A minute-by-minute speaking guide designed to perfectly communicate the system's depth.
* **[Commercialization & SaaS Strategy](COMMERCIALIZATION_STRATEGY.md)**
  * High-level business plan mapping target markets (CROs, Universities) and the platform's immediate competitive moat.
* **[Academic Role-Based Navigation Plan](plan.md)**
  * A workflow guide tailored for researchers, professors, undergraduate students, and data engineers. Instructs each persona on exactly how to use the software.
* **[UI/UX Design System](UI_UX_DESIGN_SYSTEM.md)**
  * Documentation for the custom "Crystalline Obsidian" CSS variables overriding Streamlit defaults.
* **[AI Prompt Engineering Protocols](PROMPT_ENGINEERING.md)**
  * Demonstrates the JSON schema grounding procedures used to stop the Anthropic/Gemini engines from hallucinating.
* **[Ethics & Safety Compliance](ETHICS_AND_SAFETY.md)**
  * Details our stance on dual-use bio-security risks and the hardcoded mathematical rejection of neuro-toxins.
* **[Contributing Guidelines](CONTRIBUTING.md)**
  * System rules for developers to isolate RDKit errors in `except` blocks and branch efficiently.
* **[System Changelog](CHANGELOG.md)**
  * Complete milestone history (up to the v1M Omnipotent build).
* **[Team Contributions Manifest](CONTRIBUTIONS.md)**
  * Outlines how diverse academic skill sets fused to build the product.
* **[Project License (MIT)](LICENSE.md)**
  * Open source rights and permissions logic.
