# ⬡ ChemoFilter: Security & Operational Compliance

As a computational platform operating with potentially proprietary or un-patented intellectual property (SMILES strings), maintaining data containment is critical. This document explicitly outlines how the platform handles data.

---

## 1. Local-First Processing (Zero Leakage)
*   **The Problem:** Using typical web-based tools like *SwissADME* requires uploading unpatented molecular blueprints to an external Swiss server. This breaks provisional patent confidentiality.
*   **The ChemoFilter Protocol:** The core mathematical engine operates entirely within the host CPU. RDKit C++ generation, Molecular Mass mapping, and LeadScore generation happen strictly in the isolated `data/compounds.parquet` buffer.
*   **Network Isolation:** If the machine is disconnected from the WiFi, the platform will continue generating 100% of numerical/heuristic analytics offline.

## 2. Cryptographic Endpoint Calling
When the `ai_explainer_tab.py` queries the Anthropic API to generate a narrative pharmacological summary:
1. The SMILES string and metrics are packaged.
2. The package is hashed: `hashlib.sha256(payload.encode()).hexdigest()`.
3. If this exact molecule has been processed previously on that machine, the Anthropic query is forcefully cancelled by the UI interceptor securely. 

## 3. Disabling Cloud Telemetry
As of the `1M` Omnipotent build, all external telemetry to the `.gemini` database or `cid.cloud_engine` is bypassed locally unless explicitly opted in via `.env` keys. Users can safely operate under full offline compliance without generating server-logs.
