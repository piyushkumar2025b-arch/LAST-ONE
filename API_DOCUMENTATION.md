# ⬡ ChemoFilter: Network & API Documentation

ChemoFilter isn't just an offline mathematical calculator—it sits at the center of a dense computational web, intelligently pulling contextual data from global biology databases and AI inference models.

This document explicitly outlines the security, pacing, and architecture of the `api_manager.py` network layer.

---

## 1. External Network Endpoints

The platform connects to three primary external systems:

1.  **PubChem PUG REST (NCBI)**
    *   **Usage:** Resolving unknown SMILES strings into IUPAC nomenclature and known synonyms (e.g., converting `CC(=O)Oc1ccccc1C(=O)O` into `Aspirin`).
    *   **Method:** GET requests matching canonical SMILES against PubChem CIDs.
2.  **ChEMBL API (EMBL-EBI)**
    *   **Usage:** Extracting macroscopic bioactivity. If a generic structure matches a known ChEMBL target, the API pulls relevant IC50 / EC50 protein affinities to generate drug-repurposing insights.
3.  **Anthropic API (Claude 3)**
    *   **Usage:** The `ai_explainer_tab.py` compiles the generated descriptors (QED, HBD, Lipinski violations) into a dense text prompt, sending it to Claude. The model returns narrative, readable translations for non-chemists.

---

## 2. API Security & Rate-Limit Defense

Calling external servers during a 1,000-compound batch process will instantly trigger a `HTTP 429 Too Many Requests` ban. The ChemoFilter Network Layer implements professional-grade defenses to prevent crashes.

### Defense I: Jittered Exponential Backoff
Inside `api_managers.py`, no HTTP request is sent "naked." Every request is wrapped in a discrete retry loop.
*   **Trigger:** If the server rejects the request (Status Code 429 or 503).
*   **Action:** The system pauses execution for a mathematically scaling duration based on the exponent of the retry attempt: `delay = Base * (2 ^ Attempt)`.
*   **Jitter Injection:** Pure exponential backoff can cause a "Thundering Herd" problem where multiple threads hit the server at the exact same retry second. The platform resolves this by injecting a randomized scalar noise (`Jitter`) forcing the retries to stagger safely.

### Defense II: Local Vector Caching (Cryptographic)
External calls are expensive.
*   Before hitting the web, the platform converts the payload and the endpoint URL into a string.
*   This string is hashed: `id = hashlib.sha256(payload).hexdigest()`.
*   The system searches the local `st.session_state` RAM. If the hash exists, it aborts the network socket entirely and returns the saved JSON, eliminating redundant bandwidth.

### Defense III: Graceful Degradation (Circuit Breakers)
If you are analyzing SMILES offline on an airplane, the application will not crash.
*   `api_reliability.py` dictates strict timeout windows (e.g., 2.5 seconds). 
*   If the router timeout is exceeded, the Circuit Breaker trips. 
*   The main RDKit engine continues unharmed, and the UI simply replaces the specific API component with a graceful warning (`"External API unreachable — Proceeding with local topological calculus."`).
