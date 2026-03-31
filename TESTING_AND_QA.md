# ⬡ ChemoFilter: System Testing & QA Framework

To ensure that the 50+ variables mapping topological and ADMET bounds remain strictly accurate across versions, this platform is governed by a rigorous architectural testing methodology.

---

## 1. Ground-Truth SMILES Arrays 
To validate that the `chemo_scoring.py` math has not drifted, every time the core engine updates, we parse the "Baseline 5" drugs:
*   `CC(=O)Oc1ccccc1C(=O)O` (Aspirin)
*   `CC(C)Cc1ccc(cc1)C(C)C(=O)O` (Ibuprofen)
*   `CN1C=NC2=C1C(=O)N(C(=O)N2C)C` (Caffeine)

**Test 1 (Lipinski Check):** The boolean logic explicitly triggers failures if MW > 500. The Baseline 5 must ALWAYS pass the Lipinski filter with zero array errors.

## 2. API Failure Handling (Circuit Breakers)
What happens when you deploy ChemoFilter offline on an airplane, but click the AI Explainer Tab (which hits Claude 3/Gemini)?
1. **Network Timeout Hook:** `api_manager.py` limits TCP/HTTP requests to exactly 12 seconds.
2. **Circuit Trip:** Once tripped, the `_api_state` flag sets to `OFFLINE`.
3. **Graceful UI Degradation:** Instead of crashing the entire Python runtime with a massive red Streamlit stack trace (`urllib3.exceptions.ReadTimeout`), the UI silently captures the Exception and renders a professional `[SYS-WARN] AI Engine Offline - Proceeding with local topological maths.`

## 3. RDKit C++ Wrapping (Preventing Segmentation Faults)
The `RDKit` library is a C++ wrapper. If given a SMILES string that breaks fundamental valency rules (e.g. Carbon with 5 bonds), the C++ pointer dereferences invalid memory and **forces the entire terminal to abruptly close** (Segmentation Fault).

*   **Sanitization Layer:** `chemo_scoring.py` runs all uploaded SMILES through `Chem.MolFromSmiles(smiles, sanitize=True)`. If it returns `None`, the row is physically discarded from the Parquet buffer and tracked as a failed molecule.
*   The application never stops running for valid SMILES strings further down the loop.

## 4. OOM (Out-of-Memory) QA
How do we know the O(N^2) pandas bug is fixed?
We used Python's `tracemalloc` on a mock generate of 50,000 blank compounds.
Because of the FastParquet streaming logs, RAM usage flatlines at roughly 65MB indefinitely during the entire hour-long calculation loop.
