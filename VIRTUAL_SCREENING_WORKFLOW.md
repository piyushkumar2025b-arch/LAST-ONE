# ⬡ ChemoFilter: Virtual Screening Workflow (Step-by-Step)

**A Technical Guide to Running 1,000+ Compounds Through the 9-Tier Pipeline**  
*The "Chemo-Standard-Operating-Procedure" (SOP)*

---

## 1. Executive Overview

Virtual Screening is the most common use case for ChemoFilter. For scientists who have a library of SMILES strings (e.g., from a commercial supplier or a previous SAR study), we have codified a standard 5-Step Workflow for effective triage.

---

## 2. Step 1: Input & Sanitization

1.  **Format:** ChemoFilter accepts strings (SMILES) or .SDF (Structure-Data File).
2.  **Canonicalization:** Every string is passed through **RDKit Sanitization** to remove valence errors and standardize aromaticity.
3.  **SHA-256 Hashing:** Assigning a unique ID to each compound to prevent redundant re-processing.

---

## 3. Step 2: The "Vanguard" Tier 1 Filter

The **Tier 1 (Vanguard Core)** acts as the first gateway.

*   **Logic:** Filter out any molecule that violates more than TWO of **Lipinski's Rules**.
*   **Result:** This instantly reduces the dataset by ~20–40%, removing "chemical junk" and focusing on orally active leads.

---

## 4. Step 3: Progressive Processing (Tiers 3–7)

Once the "Vanguard" identifies potential leads, the system triggers the higher tiers:

1.  **Tier 3:** Calculate **ESOL Solubility**.
2.  **Tier 5:** Calculate **Synthetic Accessibility (SA)**.
3.  **Tier 7:** Run **Metabolic Stability** and **hERG Liability** alerts.

**Temporal Note:** Tiers 1-5 run in sub-second time. Tier 7 takes $\approx$ 1s per compound.

---

## 5. Step 4: Tier 9 "Global" Quantum Triage

Only the **Top 5% of leads** (based on the `Lead_Score`) should be passed to **Tier 9 (Aether Engine)**.

*   **Logic:** Calculate 3D-MORSE descriptors and WHIM shape indices ($O(N^3)$).
*   **Significance:** This final gate ensures the molecules are not just "drug-like" on paper, but have the specific 3D topography needed for receptor binding.

---

## 6. Step 5: AI Interpretation & Final Research Report

The final step is to activate the **Anthropic Claude AI Interpreter**:

1.  **Context Injection:** The system sends a numerical ADMET summary for the top 5 candidates.
2.  **Rationale Generation:** The AI writes a pharmacological summary explaining the pros and cons of each lead.
3.  **CSV/JSON Export:** Download the final 1,000-compound dataset (with all Tier 1–9 descriptors) for internal lab review.

---

## 7. Summary Triage Checklist

*   [ ] SMILES Sanitization (0.01s/cmpd)
*   [ ] Lipinski Ro5 Filter (Tier 1)
*   [ ] ESOL Solubility Analysis (Tier 3)
*   [ ] Synthetic Accessibility Check (Tier 5)
*   [ ] High-Risk hERG/Toxicity Analysis (Tier 7)
*   [ ] Quantum Structural Triage (Tier 9 - Top 5% only)
*   [ ] Final LLM-Backed Lead Identification (Top 1–5 candidates)
