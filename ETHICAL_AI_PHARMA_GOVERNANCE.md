# ⬡ ChemoFilter: Ethical AI & Pharmacology Governance

**Human-in-the-Loop Philosophy for AI-Driven Drug Discovery**  
*The Policy of Oversight for LLM-Generated Pharmacological Rationales*

---

## 1. Executive Overview

Large Language Models (LLMs) such as Anthropic Claude 3 and Google Gemini can generate confident but biologically incorrect rationales—a phenomenon known as "hallucination." In the context of drug discovery, a hallucination could lead to a toxic compound being incorrectly labeled as safe.

**ChemoFilter** addresses this by using a **"Strictly Scientific Anchor"** approach in `ai_explainer_tab.py`, ensuring that every AI rationale (Claude / Gemini) is anchored to the raw numerical ADMET indices.

---

## 2. The Multi-Step "Prompt Anchor" Protocol

Before any AI Rationale is generated:

1.  **Data Extraction:** The system extracts the raw numerical ADMET profile (MW, LogP, TPSA, Fsp3, hERG, PAINS).
2.  **Context Loading:** A pre-curated "Expert Dictionary" of scientific terms is injected into the prompt.
3.  **Numerical Enforcement:** The prompt explicitly states: *"Base your rationale ONLY on the provided numerical indices. Do NOT invent values for metrics not in the provided matrix."*
4.  **Verification:** The system compares the LLM's final conclusion to the `Lead_Score`. If the AI says "Excellent Lead" but the score is $<20$, the system throws an **"AI Conflict Alert"**.

---

## 3. Transparency & Interpretability (XAI)

We follow the **Explainable AI (XAI)** methodology:

*   **Logic:** Don't just give a "Yes" or "No." 
*   **Result:** Every AI rationale includes a **"Scientific Evidence"** block citing why a certain conclusion was reached (e.g., *"Lead rejected due to PAINS flag at C-center 4"*).

---

## 4. Bias Mitigation in Pharmacology

ADMET models are often biased towards "Small, Hydrophobic Molecules" (the classical Rule of Five). ChemoFilter mitigates this by:

1.  **Diversity Normalization:** Comparing results against **200+ FDA-approved drugs** across all chemical classes (peptides, macrocycles, small molecules).
2.  **Constraint-Free Tiers:** Tier 9 (Aether) uses purely topological descriptors that do not rely on "historical bias" but on the physical shape of the molecule.

---

## 5. Dual-Use & Biosecurity

Drug discovery software could theoretically be used to design toxins or chemical weapons. ChemoFilter addresses this by:

*   **Restricted Access:** The **"Toxicological Hazard"** filter in Tier 7 is biased towards identify *liability* rather than *efficacy* of lethal payloads.
*   **Audit Logging:** Every molecule processed is recorded in the **WAL (Write-Ahead Log)** with an immutable SHA-256 hash for accountability.

---

## 6. How to Extend Ethical Controls

Phase 5 (Future Roadmap) involves the integration of a **"Red-Teaming"** AI agent that reviews all lead suggestions specifically to identify potential safety hazards or biosecurity risks before they are presented to the user.
