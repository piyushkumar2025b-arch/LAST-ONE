# ⬡ ChemoFilter: Local Installation & Setup Guide

Due to the heavy C++ bindings required for topological chemistry (`RDKit`) and the sophisticated $O(1)$ memory requirements for columnar storage (`fastparquet`), proper installation is critical. Follow this guide to boot ChemoFilter safely on your local machine.

---

## 1. System Requirements
*   **Operating System:** Windows 10/11, macOS (M-series supported via Rosetta/native conda), or Linux (Ubuntu/Debian preferred).
*   **Python:** Version 3.9 through 3.11. *(Note: Extreme edge-case compatibilities with Python 3.12+ may break older RDKit builds).*
*   **Memory:** Minimum 4GB RAM (The system handles 10,000+ compounds using $<50$MB RAM due to Parquet streaming, but Streamlit UI requires baseline resources).

## 2. Environment Configuration

### Step 2.1: Clone the Repository
Download the project to your local drive. Do not run this on a networked drive (e.g., OneDrive) if you are experiencing heavy read/write latency, as the JSONL Write-Ahead Log operates continuously.
```bash
git clone https://github.com/your-username/ChemoFilter.git
cd ChemoFilter
```

### Step 2.2: Virtual Environment Setup
It is **strictly required** to use a virtual environment. Installing RDKit globally can corrupt other Python computational pipelines.
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

## 3. Dependency Installation (RDKit Nuances)

Historically, `RDKit` required complex Conda environments. This platform has been configured to use the compiled PyPI wheels for speed.
```bash
pip install -r requirements.txt
```

**Critical Dependencies Included:**
*   `rdkit` or `rdkit-pypi` (Core chemistry C++ bindings)
*   `streamlit` (Frontend functional rendering)
*   `fastparquet` & `pandas` (Tabular data routing)
*   `plotly` (WebGL scatter rendering)
*   `requests` (API networking)

## 4. API & Secrets Management (Optional but Recommended)

To utilize the **🤖 Mechanistic Result Interpretation Engine** and external macromolecule binding database, you must configure your API keys. 

1. Create a hidden directory in the project root: `mkdir .streamlit`
2. Create `secrets.toml` inside that directory: `touch .streamlit/secrets.toml`
3. Add your keys:
```toml
# .streamlit/secrets.toml

# Anthropic Claude 3 (Required for AI Narrative Tab)
ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx"

# Optional: Google Gemini / OpenAI Fallbacks
GOOGLE_API_KEY = "AIzaSyxxxxxxxxxxxxxxxxxxxxxxxx"
```
*Note: ChemoFilter includes fail-safes. If no keys are provided, the local RDKit mathematical engine still functions 100%. Only the qualitative AI narrative tab disables itself.*

## 5. Boot Sequence

Launch the master orchestrator.
```bash
streamlit run app.py
```
*   The system will dynamically compile the Crystalline Obsidian CSS and open `http://localhost:8501` in your default browser.
*   **To Test System Integrity:** Do not type SMILES manually. Click the **"🚀 Demo Mode"** button on the landing page to trigger the 5-drug baseline evaluation sweep. If the Final Conclusion tab populates, your local environment is perfectly configured.
