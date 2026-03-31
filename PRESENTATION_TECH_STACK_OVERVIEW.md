# ⬡ ChemoFilter: Technology Stack Overview (1-Pager)

**The Multi-Disciplinary Stack for Drug Discovery v1.0.0**  
*The Tools and Technologies Powering the 9-Tier Engine*

---

## 1. Executive Overview

ChemoFilter was built to be a bridge between high-end scientific modeling and modern web interactivity. This "Showcase Stack" was chosen for its **Speed**, **Privacy**, and **Modularity**.

---

## 2. Core Cheminformatics (The Logic)

1.  **RDKit (C++ Kernel):** The gold standard for molecular sanitization, fingerprinting, and 2D/3D descriptor math. 
2.  **ETKDG v3:** Experimental-Torsion Knowledge Distance Geometry for 3D conformer generation.
3.  **MMFF94:** Merck Molecular Force Field for energy minimization.

---

## 3. Data Engineering (The Backbone)

*   **FastParquet + Snappy:** Columnar, compressed storage for O(1) data scaling up to 1 Million+ compounds.
*   **WAL (Write-Ahead-Log):** JSON-L based persistence layer for zero data-loss during app crashes.
*   **Redis (Local):** Fingerprint caching to prevent redundant $O(N^3)$ calculations.

---

## 4. Artificial Intelligence (The Interpreter)

| AI Engine | Model | Role |
| :--- | :--- | :--- |
| **Anthropic** | Claude 3.5 Sonnet / Haiku | Primary pharmacological rationale generator. |
| **Google** | Gemini 1.5 Pro / Flash | Secondary research agent (PubChem/PubMed summary). |
| **SBERT** | All-MiniLM-L6-v2 | Semantic similarity between lead descriptions. |

---

## 5. User Interface (The Presentation)

*   **Streamlit (v1.32.0):** Rapid analytical web deployment and session state orchestration.
*   **Custom CSS (Crystalline Obsidian):** Glassmorphism, Neon Cyan highlights, Toxic Orange hazards.
*   **Plotly & Py3Dmol:** Interactive 3D structural mapping and conformational explorers.

---

## 6. Hosting & Cloud (Scaling)

| Tier | Status | Platform |
| :--- | :--- | :--- |
| **Local (Showcase)** | **Active** | Windows / macOS / Linux. |
| **Cloud (Cluster)** | **Phase 4** | AWS / Azure / GCP (Dask-Distributed). |
| **Mobile** | **Phase 5** | PWA (Progressive Web App) wrapper. |

---

## 7. How to Maintain the Stack

The `dependency_registry.py` module tracks all Python package versions. To update the stack:
1.  Navigate to `requirements.txt`.
2.  Update the specific library (e.g. `rdkit`).
3.  Run the **"Vanguard Sanity Check"** in `app.py` to ensure zero regression in the 9-Tier Processing Engine.
