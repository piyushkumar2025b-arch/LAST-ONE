# ⬡ ChemoFilter: Developer Onboarding & Contribution Guide

**A Technical Guide to the 9-Tier Engine and "Crystalline Obsidian" UI**  
*Building the Future of Open-Source Computational Triage*

---

## 1. Executive Summary: Core Philosophy

ChemoFilter was built as a "Highly Coupled Science, Highly Decoupled Engineering" platform. This means that while the **ADMET calculations** (RDKit) are deeply interconnected, the **Software Modules** (Tiers, API Manager, UI) are isolated.

---

## 2. Setting Up Your Development Environment

To begin contributing to ChemoFilter, follow the 3-Step Setup in [SETUP.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/SETUP.md):

1.  **C++ Backdoor:** Ensure you have the **Visual Studio Build Tools (C++)** installed, as `rdkit` and `fastparquet` require C-compilation.
2.  **Parquet Tooling:** Use a tool like **Parquet Viewer** or the `pandas.read_parquet` function in a Jupyter Notebook to inspect the `data/compounds.parquet` database.
3.  **Secrets:** You **must** have an **Anthropic API Key** to test the "AI Explainer" tab.

---

## 3. The 9-Tier Processing Engine Logic

Every analytical tier is its own module (e.g., `features_v15.py`, `aether_engine_v10000.py`).

*   **To Add a New Tier (Tier 11):**
    1.  Create `system_v11000.py`.
    2.  Define a function `compute_tier_11(smiles, mol)`.
    3.  Add the tier to the `engine_orchestrator.py` registry.
    4.  Update `app.py` with a new `st.tab()` to display the Tier 11 results.

---

## 4. UI/UX: The "Crystalline Obsidian" Style

The UI is built on a custom CSS layer injected in `app.py`.

*   **Design Tokens:** We use HSL-tailored colors (Obsidian blacks, Neon-Cyan accents). Avoid using standard Streamlit "Red" or "Blue" buttons.
*   **Metric Cards:** Use the `render_metric_card()` function from `chemo_ui_components.py` to maintain a consistent gloss-finish aesthetic for all ADMET values.
*   **Skeleton Loaders:** When adding a new long-running calculation, always wrap it in a `st.empty()` or a non-blocking HTML loader to keep the UI fluid.

---

## 5. Branching & PR Strategy (Internal)

1.  **Feature Branching:** Use `feature/[tier-name]` for all new engine tiers.
2.  **Linting:** We enforce **PEP 8** standards. Use `ruff` or `flake8` before committing.
3.  **Testing:** Every new mathematical engine must have a corresponding test case in `advanced_testing_modes.py` to verify its accuracy against **aspirin** baseline values.

---

## 6. How to Propose a New Scientific Metric

If you wish to add a new descriptor (e.g., **LogD at pH 7.4**):
1.  Verify the source in [references.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/references.md).
2.  Implement the Delaney-style regression in the relevant Tier module.
3.  Document the math in [ALGORITHMS_AND_MATH.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/ALGORITHMS_AND_MATH.md).
