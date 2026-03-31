# ⬡ ChemoFilter: Bioisostere Replacement Database

**The Standardized Library of High-Probability Structural Substitutions**  
*Curated Mappings Used by the "Bioisostere Hopper" Module (Tier 5)*

---

## 1. Executive Overview

**Bioisosteres** are groups with similar electronic or spatial properties. Replacing a functional group with its bioisostere allows a chemist to improve potency, reduce toxicity (e.g., $hERG$), or bypass a patent. **ChemoFilter** uses a local library of 2,000+ FDA-proven bioisosteres to suggest high-probability structural variations of a lead.

---

## 2. Common Bioisostere Mappings (The Rule of 50)

ChemoFilter's `scaffold_hopper.py` uses these standardized mappings to "Morph" a lead:

| Original Group | Suggested Bioisostere | Scientific Logic | Resulting Change |
| :--- | :--- | :--- | :--- |
| **$-H$** | **$-F$** | Isostere (Same size). | Increased metabolic stability. |
| **$-CH_3$** | **$-NH_2$ / $-OH$** | Similar size/electronics. | Higher solubility, potentially lower LogP. |
| **Phenyl Ring** | **Pyridine / Thiophene** | Isosteric Rings. | Higher solubility, different pKa. |
| **$-COOH$** | **Tetrazole** | Bioisosteric Acid. | Better membrane permeability. |
| **$-CONH_2$** | **Triazole / Imidazole** | Amide Mimicry. | Increased stability to proteases. |

---

## 3. The 3-Step "Morph" Selection Sequence

When the user activates the "Bioisostere Hopper" in the UI:

1.  **Logic:** Identification of "High-Risk" atoms (e.g., in a **PAINS** or **hERG** alert).
2.  **Action:** The system queries the **Bioisostere Replacement Database** for the $O(1)$ most similar groups.
3.  **Result:** Five alternative candidates are generated and automatically screened via the **9-Tier Engine**.

---

## 4. Visualizing Similarity: The "Morph-Cloud" PCA

The UI displays the morphed leads in a **PCA Projection (The Morph-Cloud)** where:

*   **Logic:** Proximity in the cloud indicates structural similarity.
*   **Significance:** A "Good Morph" maintains a Tanimoto similarity of **0.6 to 0.8** with the original lead.

---

## 5. Significance in Intellectual Property (IP)

Most "New Drug" patents are built on finding a bioisotere for a known active compound. ChemoFilter enables this "Freedom to Operate" analysis by suggesting structural variants that are different enough to be patentable but similar enough to maintain target binding.

---

## 6. How to Extend This Database

Phase 4 (Roadmap) includes a **Federated Bioisostere Library**, where institutional users can upload their own proprietary bioisosteres from successful lab campaigns to improve the engine's predictive accuracy.
