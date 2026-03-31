# ⬡ ChemoFilter: AI Hallucination Mitigation Protocol (AHMP)

**Ensuring Scientific Accuracy in LLM-Generated Pharmacological Rationales**  
*The "Prompt Anchor" and "Numerical Enforcement" Architecture*

---

## 1. Executive Overview

Large Language Models (LLMs) are prone to "hallucinations"—generating confident but biologically incorrect data. In drug discovery, this is a **Critical Risk.** **ChemoFilter** addresses this by using the **AHMP Protocol** in `ai_explainer_tab.py`, ensuring that every AI rationale (Anthropic Claude 3 / Gemini) is anchored to the raw numerical ADMET indices.

---

## 2. The "Shield" Prompt Architecture

Before the user sees the "AI Interpretation," the system executes a **4-Layer Prompt Construction**:

| Layer | Component | Scientific Goal |
| :--- | :--- | :--- |
| **Layer 1** | **Numerical Anchor** | Injecting the $MW, LogP, TPSA, Fsp3$ and $SA$ indices directly from RDKit. |
| **Layer 2** | **Expert Dictionary** | Injecting the definitions of metrics from `terminology.py` to prevent "Semantic Drift." |
| **Layer 3** | **Constraint Enforcement** | Explicitly stating: *"Base your rationale ONLY on the provided matrix. Do NOT invent pKa or $Vd$ values if they are not in the provided row."* |
| **Layer 4** | **Structure-Property-Logic** | Requiring the LLM to explain "The Why" based on structural motifs (e.g., *"Lead rejected due to high aromatic ring count affecting solubility"*). |

---

## 3. The "Conflict Guard" Mechanism

If the AI generates a conclusion that is mathematically impossible based on the **Vanguard Core (Tier 1)** results:

*   **Logic:** A comparison between the LLM's **Sentiment (0.0 to 1.0)** and the **Lead_Score (0 to 100)**.
*   **Result:** If a molecule fails the Lipinski rule but the AI says "Excellent Candidate," the system throws a 🔴 **"Scientific Conflict Detected"** alert.

---

## 4. Mitigation Table: Error vs. System Defense

| Potential Hallucination | AHMP Shield Mechanism |
| :--- | :--- |
| **"This molecule is an excellent CNS drug"** | TPSA check: If $TPSA > 90$ Å², the system appends a **"BBB Permeability Warning"** to the output. |
| **"Solubility is high"** | ESOL logS check: If $log S < -6.0$, the system forces the AI to acknowledge the **"Insolubility Risk."** |
| **"Structure is trivial to synthesize"** | SA_Score check: If $SA > 6.0$, the system highlights the **"Synthetic Complexity Penalty."** |

---

## 5. Visualizing the "Audit Trail"

The **"Mechanistic Rationale"** tab includes a **"View Raw Context"** button:

*   **Value:** It shows exactly which numerical values were sent to the AI.
*   **Transparency:** This "Human-in-the-Loop" verification is a cornerstone of the **VIT MDP 2026** ethics requirements.

---

## 6. Future: Self-Correction (Phase 5)

Phase 5 Roadmap involves a **"Critic Agent"** (a second LLM instance) that reviews the primary rationale for any scientific hallucinations before it is presented to the user.
