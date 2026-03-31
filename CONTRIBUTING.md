# ⬡ ChemoFilter: Contributing Guidelines

Thank you for considering contributing to the ChemoFilter engine. Building an omnipotent drug-discovery platform requires explicit multidisciplinary precision. Please adhere to these guidelines when submitting Pull Requests (PRs).

---

## 1. Branch Strategy
We adhere to strict Git-flow architecture.
*   **`main`:** Contains production-ready code with guaranteed zero unhandled exceptions. This branch is protected.
*   **`develop`:** Integration branch. All new chemistry features must merge here first.
*   **`feature/[name_of_heuristic]`:** Example: `feature/caco2_permeability`.

## 2. Test Coverage & Module Boundaries
If you are adding a new prediction algorithm (e.g., Blood-Brain Barrier disruption or Renal Clearance limits) to `chemo_scoring.py`:
1.  **Wrap it properly:** RDKit will fault if passed an invalid graph. Every function MUST be wrapped in `try/except Exception: return None`. Do not let a single SMILES failure bring down the entire 10,000-compound Streamlit sequence.
2.  **No Pandas Appends:** Never import `pandas` to manipulate the memory store. Feed your scalar variables directly into the `fastparquet` stream via `data_engine.py`.

## 3. Creating a Local Environment
1.  Fork the repo and clone locally.
2.  Create an isolated virtual environment (`venv`).
3.  Install via `pip install -r requirements.txt`.
4.  Ensure `rdkit-pypi` installs correctly.
5.  If contributing to the **🤖 Mechanistic Result Interpretation Engine**, you must create `.streamlit/secrets.toml` locally with your own API key. Do not commit keys to GitHub.

## 4. Submitting a Pull Request
*   Use the standard ChemoFilter PR Template.
*   Include the mathematical formula you implemented in the comments.
*   Link to the peer-reviewed paper (e.g., *Baell 2010*) proving your limit is scientifically sound.

## 5. Security Vulnerabilities
If you discover a severe cache-poisoning vulnerability in the `SHA-256` payload routing or a data leak regarding proprietary SMILES caching, do NOT open a public issue. Email the project maintainers directly via `Piyush Kumar` to execute a stealth patch.
