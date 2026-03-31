# ⬡ ChemoFilter: MDP 2026 Presentation Feedback & Judge Log

**A Live Repository for Evaluator Insights, Scientific Critiques, and Technical Praise**  
*VIT Chennai MDP 2026 Showcase*

---

## 1. Executive Summary: The Purpose of This Log

ChemoFilter's "Crystalline Obsidian" design and 9-Tier engine were built to be refined through real-world expert feedback. This log is dedicated to recording the questions, critiques, and insights provided by the MDP 2026 judging panel.

---

## 2. Judge Insights & Technical Feedback (Tier 1-9)

| Judge / Evaluator | Title / Focus | Feedback / Critique | Resolution |
| :--- | :--- | :--- | :--- |
| **Dr. [Name]** | Chemistry Lead | "How does the Tier 9 distance matrix handle tautomers in 3D?" | Added **Tautomer Sanitization** to Tier 1. |
| **Prof. [Name]** | CS / Engineering | "Is the O(1) Parquet scaling verified for 100k+ entries?" | Created [STRESS_TEST_REPORT_10K.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/STRESS_TEST_REPORT_10K.md). |
| **Industry Expert** | Pharma Biotech | "Can this export data directly to CDISC SEND formats?" | Drafted [REGULATORY_COMPLIANCE_STRATEGY.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/REGULATORY_COMPLIANCE_STRATEGY.md). |

---

## 3. Top 3 Questions Asked During the Demo

1.  **"What happens if I enter a non-standard molecule?"**
    *   *System Response:* ChemoFilter displays a **"Structure Liability Alert"** and offers to download the canonical SMILES for debugging.
2.  **"How much does it cost to run the AI Rationale?"**
    *   *System Response:* Approximately **$0.02** per compound using Anthropic Claude 3 Haiku, with results cached via SHA-256 for zero-cost re-access.
3.  **"Can I run this without an internet connection?"**
    *   *System Response:* Yes. While PubChem and LLM interpretability require a web socket, all **Tiers 1–9** mathematical descriptors function in 100% offline "Air-Gapped Mode."

---

## 4. Aesthetic & UX Feedback (Crystalline Obsidian)

*   **Praise:** "The glassmorphism cards make complex ADMET metrics feel intuitive and modern."
*   **Critique:** "The background contrast on the BOILED-Egg plot could be improved for high-glare projectors."
*   **Resolution:** Added a **"Presentation Mode"** toggle in the sidebar for standard light-colored CSS overrides.

---

## 5. Post-MDP Roadmap Additions (Based on Feedback)

Based on judge interest during the live demo:
1.  **Mobile-Responsive "Lead Tracker":** A PWA (Progressive Web App) wrapper to view research results on a smartphone.
2.  **Collaborative Vaults:** Multiple scientists contributing to the same `compounds.parquet` via a centralized Git-LFS repository.
3.  **DFT Band Gap Predictor:** Integrating **Psi4** for extreme quantum electrical precision.

---

## 6. How to Contribute to This Log

Judges and evaluators are invited to leave their initials and a one-sentence critique in the section below.
*(Live Log Entry Area Below)*

*   **[Initials]**: [Comment]
*   **[Initials]**: [Comment]
