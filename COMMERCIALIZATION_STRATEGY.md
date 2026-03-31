# ⬡ ChemoFilter: Commercialization & SaaS Business Strategy

Since ChemoFilter is being presented at the **VIT Chennai Management Development Program (MDP)**, evaluating the software not just as a computational script, but as an enterprise SaaS product is critical.

---

## 1. The Market Problem (Why ChemoFilter?)
The average pharmaceutical R&D pipeline costs **$2.6 Billion** and takes **10-15 years**. Over 90% of lead compounds fail in clinical trials, primarily due to unforeseen ADME (Absorption, Distribution, Metabolism, Excretion) or toxicological issues. 
Currently, biotech startups and academic labs rely on either:
*   A fragmented pipeline of open-source scripts that crash on large datasets.
*   Multi-million-dollar enterprise contracts like Schrödinger.

**ChemoFilter is positioned as the "Canva of Drug Discovery"**: An instantly accessible, highly visual, $O(1)$ scalable ADMET platform specifically targeting mid-tier biotech, CROs (Contract Research Organizations), and academic institutions.

## 2. Competitive Moat
1.  **Architecture:** The `fastparquet`-backed JSONL pipeline allows users to evaluate 50,000 compounds on a standard laptop. Competitors relying on Pandas DataFrames will crash their browser executing the same workload.
2.  **Mechanistic AI Integration:** Raw tabular data means nothing to a biologist. By wrapping Anthropic Claude / Gemini 2.5 Pro into the pipeline, ChemoFilter auto-generates pharmacological lessons out of raw Cartesian floats.
3.  **Local IP Protection:** ChemoFilter operates natively offline. This is a massive selling point for proprietary drug startups who cannot legally upload SMILES to web servers before filing patents.

## 3. Revenue Tiering Model
| Tier | Price | Features | Target Customer |
| :--- | :--- | :--- | :--- |
| **Academic Open** | Free | Base Lipinski/Veber heuristics, Offline Parquet hashing, no AI calls. | Universities, Undergrad Students |
| **Pro Researcher** | $49 / month | Unlocks Phase-2 AI Explanation Engines, API Key injections, batch CSV exports up to 10k SMILES. | PhD Candidates, Post-Doc Labs |
| **Enterprise SaaS** | $15,000 / year | Dedicated VPC deployment, Custom API Rate Limits, AutoDock Vina programmatic docking, Custom AWS scaling. | Biotech Startups, CROs |

## 4. Operational Costs (COGS)
Scaling ChemoFilter commercially is incredibly cheap due to the local-first execution.
*   **Compute:** CPU cycles used to run RDKit descriptors happen *client-side* inside the user's Streamlit local-host loop. Server footprint is effectively $0.
*   **API Inference:** The only variable cost. Using Gemini 2.5 Pro costs approximately ~$0.003 per compound summarisation. The Cryptographic `SHA-256` payload caching built into `api_manager.py` drastically drops this overhead.
