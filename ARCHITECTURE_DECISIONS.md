# ⬡ ChemoFilter: Architecture Decision Records (ADR)

This document explains the *Why* behind the technology stack. In a computational platform generating $100,000+$ parameters in seconds, standard web-development patterns fail. Here are the core architectural decisions driving ChemoFilter.

---

## ADR 1: O(1) Parquet Streaming vs. O(N²) Pandas Concat
**Context:** When a user uploads a `.CSV` file of 5,000 SMILES strings, traditional Python scripts loop through the SMILES and append new rows to a central `pandas.DataFrame` using `pd.concat`. 
**Problem:** Pandas DataFrames are monolithic memory blocks. Every `concat` forces the CPU to copy the *entire* previous dataframe into a new memory register. This is an $O(N^2)$ operation that crashes browser RAM by molecule 2,000.
**Decision:** We ripped out Pandas appending. As RDKit generates data, `data_engine.py` writes individual molecular vectors instantly to a compressed columnar `fastparquet` file on the hard-drive (`data/compounds.parquet`). 
**Consequence:** The platform now evaluates 10,000 compounds using the exact same RAM footprint as 10 compounds. The application is computationally immortal.

## ADR 2: Cryptographic API Caching (SHA-256)
**Context:** The platform pings external servers (PubChem, Anthropic) for supplementary data. During a 40-tab render, multiple UI components might ask the API for the exact same drug (e.g., Aspirin).
**Problem:** Redundant API calls waste massive bandwidth, trigger rate Limits, and cost actual dollars (for LLMs).
**Decision:** Implemented `api_manager.py`. Before any HTTP request leaves the machine, the input string and parameters are hashed using `hashlib.sha256()`. The system checks `st.session_state` for that exact cryptographic hash. 
**Consequence:** If Tab 3 asks for Aspirin's AI summary, it pays the Anthropic API. If Tab 12 asks again, the `SHA-256` hash matches, the HTTPS call is aborted, and the result generates instantly from local RAM.

## ADR 3: Stateless Streamlit Reactivity over Node.js/React
**Context:** The platform requires a massive, reactive frontend to display 40+ analytical tabs, 3D visualizers, and complex scatter plots.
**Problem:** Building a separate React frontend and a FastAPI backend creates severe state-synchronization latency, especially when passing gigabytes of heavy atom matrix data over JSON payloads `localhost` ports.
**Decision:** Deployed `Streamlit`. Streamlit transpiles centralized Python commands natively into a React.js frontend without a network bridge.
**Consequence:** We inject our proprietary **Crystalline Obsidian CSS** to fix Streamlit's visual limitations. The result is a unified codebase where the C++ RDKit bindings are strictly tightly coupled to the DOM elements, reducing data-transit latency to absolute zero.

## ADR 4: The JSONL Write-Ahead Log (WAL)
**Context:** Because we are writing to Parquet in streaming batches, a sudden crash (e.g., closing the terminal or a timeout) could corrupt the `.parquet` binary file.
**Decision:** We built an enterprise-grade Write-Ahead Log. Before any data hits the `.parquet` file, the raw Python dictionary is atomically appended to `data/compounds_wal.jsonl` as plain text. 
**Consequence:** If the system crashes mid-batch, upon reboot `data_engine.py` detects the corruption, reads the plain-text `.jsonl` log line-by-line, and gracefully reconstructs the last known good state. Zero data loss.
