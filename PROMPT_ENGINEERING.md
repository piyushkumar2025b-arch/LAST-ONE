# ⬡ ChemoFilter: AI Prompt Engineering Protocols

The **🤖 Mechanistic Result Interpretation Engine** is the bridge between a human biologist and a Cartesian mathematical engine. This document outlines the explicit prompt engineering that constrains the Gemini 2.5 Pro / Anthropic models from "hallucinating" false chemical statements.

---

## 1. Zero-Shot Bounding
When a user clicks "Analyze via AI", sending raw numbers (like `MW: 450, LogP: 4`) to a Large Language Model often generates verbose, hallucinated paragraphs.
To enforce scientific rigidity, ChemoFilter intercepts the user request and injects a "System Master Prompt".

**The Engine's Core Prompt Payload:**
```json
{
  "role": "user",
  "content": "You are an expert medicinal chemist. Write exactly 4 sentences: (1) overall lead assessment, (2) key ADMET strengths, (3) key liabilities, (4) one structural improvement. No markdown, no lists. DATA: {data_str}"
}
```

## 2. Token Optimization
The JSON mapping above guarantees:
1.  **Deterministic Output:** Instructing "exactly 4 sentences" physically forces the LLM to output a dense summary, capping inference tokens massively (saving bandwidth costs).
2.  **No Markdown:** By explicitly preventing the model from outputting bolded fonts (`**`) or bullet point lists (`-`), the Streamlit UI natively parses the text into the `text-muted` glowing typography without breaking the Crystalline Obsidian CSS constraints.
3.  **Role Playing:** Instructing the model to act as "an expert medicinal chemist" biases the neural weights toward peer-reviewed terminology (e.g. `Bioisosteres`, `Hepatic Clearance`) rather than colloquial biology.

## 3. Structural Analogue Generation (Bioisosteres)
When the user requests structural optimizations, the system actively forces the LLM to output in strict JSON format.

```json
{
  "role": "user",
  "content": "Medicinal chemist — suggest 3 structural analogues improving drug-likeness. SMILES: {smiles} PROFILE: {props} Return ONLY a JSON array with 3 objects, keys: smiles, change, expected_improvement. No other text."
}
```
**Why this matters:** Returning a perfect JSON string allows ChemoFilter's `eval()` loops to instantly parse the AI's suggestions and render them as native HTML data tables in the UI, rather than a raw block of copy-pasted ChatGPT text.
