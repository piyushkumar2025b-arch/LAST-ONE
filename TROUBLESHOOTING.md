# ⬡ ChemoFilter: System Troubleshooting

This document is for system administrators and developers encountering hard crashes, memory limits, or C++ binding failures within the computational engine. 

---

## 1. RDKit Segmentation Faults (C++ Level)
**Error:** The terminal instantly closes, or outputs `Segmentation fault (core dumped)`.
**Cause:** `rdkit` is attempting to parse a chemically impossible or infinitesimally broken SMILES string, causing the underlying C++ pointer to dereference invalid memory.
**Resolution:** 
1. The engine currently implements `try/except` wrapper blocks around `Chem.MolFromSmiles()`. Ensure you haven't bypassed `chemo_scoring.py` to call RDKit directly.
2. If processing a 1M+ compound chunk, pre-sanitize your dataset using the `FilterCatalog` before feeding it to the 3D conformer generation module, as MMFF94 embeddings will instantly fault on non-valant atoms.

## 2. Memory Exhaustion / OOM Kills
**Error:** `MemoryError: Unable to allocate array with shape...` or browser tab crashes.
**Cause:** You bypassed the `data_engine.py` Parquet stream and attempted to load a massive dataset fully into a single `pandas.DataFrame` or `st.session_state` list.
**Resolution:** 
1. Never hold 10,000+ generated arrays in local RAM. 
2. Ensure `FastParquet` is properly configured. If developing new modules, yield data in chunks of 500 and use `append=True` to write directly to `data/compounds.parquet`.

## 3. Anthropic API Rate Limiting (HTTP 429)
**Error:** The AI Explainer tab returns purely fallback text ("AI analysis unavailable") instead of pharmacological narratives.
**Cause:** Anthropic Claude's Tier 1 API limits are being hit (usually >5 requests per minute unless funded).
**Resolution:**
1. Wait 60 seconds. The Jittered Exponential Backoff system (`api_manager.py`) will eventually catch up.
2. Ensure the Cryptographic `SHA-256` payload caching is active. If you disable the cache, the platform will re-ping the API every time the Streamlit UI rerender loop runs.

## 4. WebGL / Plotly "Snapping" or Lag
**Error:** The 3D Conformer Explorer or the PCA Scatter Plot stutters at <10 FPS.
**Cause:** Rendering 10,000 SVG nodes natively in the DOM overloads the browser's paint buffer.
**Resolution:**
1. The platform utilizes `Plotly.WebGL` traces (`Scattergl` / `Scatter3d`) instead of standard SVG for datasets over 500 points. If the system drops back to standard SVG, check if hardware acceleration is disabled in your browser settings.

## 5. Corrupted Parquet Files
**Error:** `fastparquet.api.ParquetException: Could not open file`.
**Cause:** The application was force-killed (e.g., `Ctrl+C`) exactly during an I/O buffer write to the `.parquet` file.
**Resolution:**
1. Delete `data/compounds.parquet`.
2. The system automatically reads `data/compounds_wal.jsonl` (the Write-Ahead Log) on next boot and cleanly reconstructs the Parquet representation. Do not delete the `.jsonl` file.
