# ⬡ CHEMOFILTER — CRYSTALLINE NOIR EDITION
### 🧬 OMNIPOTENT v1,000,000 | VIT CHENNAI MDP 2026
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chemofilter.streamlit.app)
[![RDKit](https://img.shields.io/badge/RDKit-2023.09.1-orange.svg)](https://www.rdkit.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"Targeted certainty in a multiverse of chemical possibilities."**  
> ChemoFilter is a production-grade computational drug discovery and ADMET screening platform. It combines classical medicinal chemistry rules with cutting-edge Generative AI to provide researchers with an omnipotent viewing glass into molecular potential.

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [Scientific Background](#-scientific-background)
4. [Architecture Overview](#-architecture-overview)
5. [File Structure](#-file-structure)
6. [Installation & Local Development](#-installation--local-development)
7. [Deployment on Streamlit Cloud](#-deploy-on-streamlit-cloud)
8. [Usage Guide](#-usage-guide)
9. [Scoring System: ChemoScore™](#-scoring-system-chemoscore)
10. [Input Format Guide](#-input-format-guide)
11. [API & Secrets Reference](#-api--secrets-reference)
12. [Scientific References](#-scientific-references)
13. [Contributing](#-contributing)
14. [License](#-license)
15. [Acknowledgements](#-acknowledgements)

---

## ⬡ Project Overview
ChemoFilter was developed as a flagship project for the **VIT Chennai Management Development Program (MDP) 2026**. In the high-stakes world of pharmaceutical research, 90% of drug candidates fail during clinical trials—often due to unforeseen toxicity or poor pharmacokinetic properties. These "late-stage failures" cost the industry billions of dollars and years of wasted research.

ChemoFilter solves this "ADMET bottleneck" by providing a high-throughput, in silico screening vault. It allows researchers to upload libraries of thousands of compounds and instantly identify "Lead-Like" candidates while flagging "Chemical Con Artists"—compounds that may show activity in assays but are structurally flawed or toxic.

The platform's **Crystalline Noir** design language is built for professional labs, featuring a deep midnight navy aesthetic with amber-gold data anchoring. It isn't just a tool; it's a complete chemical intelligence ecosystem.

---

## 🚀 Key Features
ChemoFilter integrates over **21+ core scientific descriptors** across a massive **10-tier engine architecture**:

- **ADMET Screening**: Comprehensive Absorption, Distribution, Metabolism, Excretion, and Toxicity profiling.
- **Classic Filters**: Native implementation of Lipinski’s Rule of Five, Veber, Ghose, Egan, and Muegge filters.
- **QED (Quantitative Estimate of Drug-likeness)**: An integrated score of molecular "attractiveness" for oral drugs.
- **SA Score (Synthetic Accessibility)**: Estimating how difficult a compound is to synthesize in a wet lab.
- **Structural Alerts**: Real-time detection of **PAINS** (Pan-Assay Interference Compounds) and **Brenk** reactive groups.
- **Cardiac Liability**: Predication of **hERG** potassium channel inhibition (a major cause of cardiotoxicity).
- **Mutagenicity Risk**: Virtual **Ames** test alerts for identifying potential DNA-damaging agents.
- **Organ-Specific Profiling**:
    - **BBB**: Blood-Brain Barrier penetration modeling for CNS drug candidates.
    - **HIA**: Human Intestinal Absorption thresholds for oral delivery.
- **CYP450 Enzyme Panel**: 5-Isoform interaction analysis (3A4, 2D6, 2C9, 2C19, 1A2).
- **CNS MPO (Multi-Parameter Optimization)**: Wager’s algorithm for CNS drug alignment.
- **Solubility Models**: LogS aqueous solubility via the **ESOL** (Delaney) method.
- **Advanced Metrics**: LogD7.4, Plasma Protein Binding (PPB), Renal Clearance, and Half-life estimation.
- **Complexity Analysis**: Bertz CT complexity, Fsp3 (Fractional sp3 carbon), and heavy atom distribution.
- **Scaffold Intelligence**: Murcko scaffold decomposition and scaffold diversity analysis.
- **AI-Powered Narrative**: **Gemini 2.5 Pro** integration provides plain-language scientific explanations of complex ADMET flags.
- **Batch Processing**: Stress-tested pipelines capable of handling up to 200 compounds with recursive deduplication.
- **Export Engine**: One-click generation of PDF-ready HTML Dossiers, CSV bulk data, and JSON manifests.

---

## 🔬 Scientific Background
### ADMET: Why It Matters
ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) determines a drug's success in the human body. A compound can be highly potent against a target in a test tube, but if it doesn't reach the target (Absorption/Distribution) or is destroyed too quickly (Metabolism/Excretion), it is useless. If it kills the patient (Toxicity), it is dangerous.

### Lipinski’s Rule of Five
A rule of thumb to evaluate druglikeness. Most orally active drugs are relatively small and moderately lipophilic.
- **MW < 500 Da**
- **LogP < 5**
- **HBD < 5**
- **HBA < 10**

### PAINS & Toxicophores
**PAINS** (Pan-Assay Interference Compounds) are molecules that frequently show false-positive results in high-throughput screening. ChemoFilter uses **480+ SMARTS patterns** to filter these "nuisance compounds" out of your results.

---

## 🏗 Architecture Overview
ChemoFilter uses a unique, scalable **Layered Engine Architecture**. When you select a "Tier," the app routes your SMILES through increasingly complex tensor operations:

1.  **Vanguard Core Engine (v2.0)**: Initial structural validation and base ADMET compute.
2.  **Quantum Accuracy Engine (v30)**: LogP refinement and FDA-set similarity comparisons.
3.  **Hyper-Zenith Module (v50)**: Extended research-grade parameters.
4.  **Master Drug Atlas (v100)**: Anchoring results against 2000+ approved drugs.
5.  **Singularity Engine (v200)**: Cross-module omnipotent analysis.
6.  **Universal Analysis Engine (v500)**: Organ toxicity and pharmacophore mapping.
7.  **Celestial Engine (v1000)**: High-fidelity predictive modeling.
8.  **Omega-Zenith Engine (v2000)**: Ultimate descriptor saturation.
9.  **Xenon-God Engine (v5000)**: Supreme scoring tiers.
10. **Aether-Primality Engine (v10000)**: The final, god-mode analysis layer.

---

## 📂 File Structure
| File | Role |
| :--- | :--- |
| `app.py` | **Main Entry Point**. Injects Crystalline Noir CSS/JS and handles routing. |
| `chemo_filters.py` | **Chemical Core**. Logic for RDKit-based property calculations. |
| `chemo_scoring.py` | **Scoring Engine**. The proprietary ChemoScore™ algorithm. |
| `chemo_batch.py` | **Batch Orchestrator**. Handles multi-compound clustering and deduplication. |
| `ai_explainer_tab.py` | **AI Explainer**. Logic for Google Gemini/Claude scientific narratives. |
| `landing.py` | **Splash Page**. Animated Crystalline Noir entry experience. |
| `chemo_io.py` | **Export/Import**. Handles CSV, JSON, and PDF-HTML rendering. |
| `data_engine.py` | **Data Core**. Parquet file management and high-speed tensor ops. |
| `registry.py` | Centralized registry for all 10 tiered engine modules. |
| `packages.txt` | OS-level dependencies for RDKit (required for Streamlit Cloud). |

---

## 🛠 Installation & Local Development
### Prerequisites
- **Python 3.12+**
- Git

### SETUP
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/piyushkumar2025b-arch/LAST-ONE.git
    cd LAST-ONE
    ```
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment**
    Create a `.streamlit/secrets.toml` file:
    ```toml
    GOOGLE_API_KEY = "your_gemini_api_key_here"
    ```
4.  **Launch the App**
    ```bash
    streamlit run app.py
    ```

---

## ☁️ Deploy on Streamlit Cloud
### Automated Deployment
1.  Push your code to a GitHub repository.
2.  Log in to [Streamlit Cloud](https://share.streamlit.io).
3.  Select "New App" and point it to your `app.py` file.
4.  **Crucial**: In "Advanced Settings", add your `GOOGLE_API_KEY` to the **Secrets** section.

**Note on RDKit**: ChemoFilter includes a `packages.txt` file. This tells Streamlit to install `libxrender1` and `libxext6`, which are Linux system dependencies required for RDKit's molecule drawing library to function.

---

## 📖 Usage Guide
1.  **Enter Compounds**: Paste SMILES strings into the sidebar (e.g., `CC(=O)Oc1ccccc1C(=O)O` for Aspirin) or upload a CSV file.
2.  **Select Engine**: Use the sidebar to choose a computational tier (Aether v10000 is recommended for full dossiers).
3.  **Analyze**: The "Discovery Hub" will render the status of your compounds.
4.  **Interpret Grades**:
    - **Grade A**: Ideal Lead. High drug-likeness, low toxicity.
    - **Grade B**: Good. Minor ADMET flags, needs optimization.
    - **Grade C**: Warning. Significant liabilities.
    - **Grade F**: Rejected. High toxicity or structural alerts.
5.  **AI Insights**: Click the AI Explainer tab to get a plain-language briefing on your molecule's potential safety risks.
6.  **Export**: Scroll to the bottom to download a full scientific dossier.

---

## 📊 Scoring System: ChemoScore™
ChemoFilter uses a proprietary weighted scoring model (0-100) to rank compounds:

| Component | Weight | Criteria |
| :--- | :--- | :--- |
| **Integrity** | 20% | Structural validity, organic nature, valency checks. |
| **PhysChem** | 25% | MW, LogP, TPSA alignment with oral drug space. |
| **Potency/Discovery** | 25% | QED and Ligand Efficiency metrics. |
| **Safety** | 20% | Toxicophores (PAINS/Brenk), hERG, and Ames risk. |
| **Synthesis** | 10% | Synthetic Accessibility (SA Score) < 4.0. |

---

## 📑 Input Format Guide
### SMILES Examples
- **Ibuprofen**: `CC(C)Cc1ccc(cc1)C(C)C(=O)O`
- **Caffeine**: `CN1C=NC2=C1C(=O)N(C(=O)N2C)C`
- **Aspirin**: `CC(=O)Oc1ccccc1C(=O)O`

### CSV Upload
Your CSV should contain a column named `SMILES`. Optional columns like `ID` or `Name` will be used for labeling if present.

---

## 📚 Scientific References
1.  **Daina A, Zoete V.** *BOILED-Egg: Predictive Model for Blood-Brain Barrier Penetration and Intestinal Absorption.* ChemMedChem 11:1117 (2016).
2.  **Lipinski CA, et al.** *Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings.* Adv Drug Deliv Rev 46:3 (2001).
3.  **Delaney JS.** *ESOL: Estimating aqueous solubility directly from molecular structure.* J Chem Inf Comput Sci 44:1000 (2004).
4.  **Bickerton GR, et al.** *Quantifying the chemical beauty of drugs.* Nat Chem 4:90 (2012).
5.  **Wager TT, et al.** *Moving beyond rules: The development of a central nervous system multiparameter optimization (CNS MPO) score.* ACS Chem Neurosci 1:435 (2010).
6.  **Baell JB, Holloway GA.** *New substructure filters for removal of pan-assay interference compounds (PAINS).* J Med Chem 53:2719 (2010).
7.  **Ertl P, Schuffenhauer A.** *Estimation of synthetic accessibility score of drug-like molecules based on molecular complexity and fragment contributions.* J Cheminform 1:8 (2009).
8.  **Rogers D, Hahn M.** *Extended-Connectivity Fingerprints.* J Chem Inf Model 50:742 (2010).
9.  **Landrum G.** *RDKit: Open-source cheminformatics.* https://www.rdkit.org

---

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a Pull Request.
1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/NewFeature`).
3.  Commit your changes (`git commit -m 'Add NewFeature'`).
4.  Push to the branch (`git push origin feature/NewFeature`).
5.  Open a Pull Request.

---

## 📜 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🙏 Acknowledgements
- **VIT Chennai**: For the 2026 Management Development Program invitation.
- **RDKit Community**: For providing the world-class cheminformatics backbone.
- **Streamlit**: For the revolutionary app framework.
- **Google DeepMind**: For the Gemini 2.5 Pro API providing AI scientific narratives.

══════════════════════════════════════════════════════════════════════════════
*ChemoFilter: The Omnipotent Viewing Glass for Computational Drug Discovery.*
══════════════════════════════════════════════════════════════════════════════
