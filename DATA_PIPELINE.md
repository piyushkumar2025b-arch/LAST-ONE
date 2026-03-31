# ⬡ ChemoFilter: Data Pipeline & Parquet Routing

How does the platform process 10,000 compounds simultaneously without crashing a web browser? This document outlines the physical movement of data through the ChemoFilter engine.

---

## 1. The Bottleneck: Pandas Concat
Standard data science pipelines use `pandas.DataFrame`.
When analyzing 10,000 SMILES strings, traditional scripts look like this:
```python
df = pd.DataFrame()
for smiles in smiles_list:
    row = calculate_rdkit_parameters(smiles)
    df = pd.concat([df, pd.DataFrame([row])]) # CRITICAL ERROR
```
Every time `concat` runs, Pandas allocates brand new RAM to copy the *entire* previous dataframe. By compound #2,000, your 16GB RAM laptop will crash (an $O(N^2)$ time/space complexity nightmare).

## 2. The Solution: Streaming Parquet + Write-Ahead Logs
In ChemoFilter, arrays are strictly decoupled from the UI.
1.  **Ingestion:** The user uploads a 10,000-row `.CSV`.
2.  **Streaming Formulation:** The engine processes one SMILES at a time.
3.  **The WAL:** Before doing anything, it appends the JSON dictionary of parameters to `data/compounds_wal.jsonl`. This is a strict $O(1)$ append operation.
4.  **Parquet Compaction:** Every 500 compounds, a background Python thread picks up the JSONL file and compresses it into `data/compounds.parquet` using columnar binary storage.
5.  **Garbage Collection:** The RAM representing those 500 compounds is explicitly purged.

## 3. UI Hydration
When the user clicks the "Dashboard" tab in Streamlit, the platform does not load all 10,000 compounds into Python. 
Because it's a `.parquet` file, the UI only runs `fastparquet` queries for the specific columns needed to render a plot (e.g., retrieving `logP` and `tPSA` exclusively to render the BOILED-EGG plot), drastically minimizing memory load.

## 4. Cryptographic Caching
All AI and external Network calls are trapped in a Hash-Ring.
If `Compound A` is generated on Monday, its 40-float profile is hashed (SHA-256). 
If the user uploads an identical `Compound A` on Friday within a different 5,000-compound batch, the system detects the hash collision and blocks the computation entirely, loading Friday's result in zero milliseconds.
