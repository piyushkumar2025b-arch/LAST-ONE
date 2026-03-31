# ⬡ ChemoFilter: Data Privacy & Security White Paper

**Architecture and Implementation of a "Fully Local" Drug Discovery Suite**  
*Strategic Protection of Proprietary Chemical Intellectual Property (IP)*

---

## 1. Executive Overview

In the pharmaceutical industry, the structure of a novel drug candidate is a multi-billion dollar piece of Intellectual Property (IP). Traditional cloud-based ADMET tools (like SwissADME or pkCSM) require users to upload their SMILES strings to a remote server, creating a significant security risk for pre-patent research.

**ChemoFilter** is built on a **"Zero-Cloud"** philosophy. All core computational logic (Tiers 1–9) and structural analysis occur on the user's local machine, ensuring that proprietary chemical data never leaves the internal firewall.

---

## 2. The local-First Computational Core

ChemoFilter's dependency stack was explicitly chosen to support offline operation:

*   **RDKit (C++ Kernal):** Executes all molecular sanitization, fingerprinting, and descriptor math entirely in local memory.
*   **FastParquet:** All persistent data is stored in the `data/` directory in a compressed, columnar format.
*   **Streamlit (Local Hosting):** The UI runs on `localhost:8501`, preventing external exposure of the interface.

---

## 3. Secured External API Integrations

While ChemoFilter is "Local-First," it occasionally interacts with the web for enrichment. These connections are strictly hardened:

1.  **PubChem / ChEMBL / PDB:** Requests for public data are fired via the `api_manager.py` wrapper. No user-supplied SMILES are "uploaded" to these services; instead, they are searched via anonymized identifiers (CID) or name-basis if the user chooses.
2.  **Anthropic / Google AI (LLM Interpreters):** If the user requests an "AI Rationale" for a compound, the data sent is a **sanitized numerical matrix** (MW, LogP, TPSA) rather than the raw SMILES or IUPAC name, protecting the exact structure of the molecule.

---

## 4. Cryptographic Hashing (SHA-256)

ChemoFilter preserves the "Anonymity of Inquiry" using SHA-256 hashing. Every compound is assigned a unique identifier based on its canonical SMILES string.

*   **Cache Integrity:** If the same molecule is re-entered, the system identifies the hash and pulls the local result without ever triggering a new (and potentially visible) network request.
*   **Audit Trailing:** Hashes allow for immutable logging in the **WAL (Write-Ahead Log)** while still keeping the raw structure obscured in clear-text logs.

---

## 5. Security Checklist for Institutional Deployment

For deployment in enterprise-grade pharmaceutical labs, we recommend:

*   **Air-Gapped Mode:** ChemoFilter can run in a "Fully Disconnected" state. In this mode, web-based metadata enrichment (PubChem) is disabled, but Tier 1–9 analytical tiers remain 100% functional.
*   **Encrypted Storage:** Users are encouraged to host the `data/` directory on an encrypted bitlocker-protected partition.
*   **VLAN Isolation:** Run the ChemoFilter server on a non-routable internal VLAN to prevent cross-network UI access.

---

## 6. Future Privacy Roadmap

*   **Phase 5 (Quantum Stealth):** Integration of local GGUF-based Large Language Models (e.g., Llama 3) via the `llama-cpp-python` library to remove the need for external Anthropic/Google API keys entirely.
*   **Multi-Factor Auth (MFA):** Adding a local PIN-buffer to the `landing.py` module to prevent unauthorized local access to the research dashboard.
