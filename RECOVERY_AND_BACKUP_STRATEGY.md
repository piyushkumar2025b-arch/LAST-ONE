# ⬡ ChemoFilter: Recovery & Data Backup Strategy

**The Design and Implementation of the Write-Ahead Logging (WAL) System**  
*Ensuring Data Integrity Across Complex 9-Tier Processing Cycles*

---

## 1. Overview: The Problem of Crash Persistence

ChemoFilter handles millions of data points across 9-Tier computational engines. A standard Python session (`session_state`) is volatile; if a 3D conformational simulation crashes the kernel or if the internet connection drops during an API call, all unsaved progress is lost.

To solve this, ChemoFilter implements a **Write-Ahead Logging (WAL)** architecture in `data_engine.py`.

---

## 2. WAL Mechanism (compounds_wal.jsonl)

Before any data is written to the primary, compressed **Parquet** repository, it is first appended to a line-delimited JSON log file (`compounds_wal.jsonl`).

*   **Atomic Appends:** Each line in the WAL is a complete, standalone JSON object representing a single molecule's state. 
*   **Write Speed:** $O(1)$ disk append time. No file rewriting or memory re-allocation occurs.
*   **Persistence:** Even if the Streamlit app is force-closed, the WAL contains the exact last known state of every compound in the pipeline.

---

## 3. The 3-Step Recovery Sequence

Upon rebooting `app.py`, ChemoFilter executes the following recovery logic:

1.  **Parquet Check:** The system reads the `data/compounds.parquet` database to establish the baseline of "fully committed" data.
2.  **WAL Reconciliation:** The system reads the `compounds_wal.jsonl` file and compares the UUIDs (SHA-256 hashes) with the Parquet database.
3.  **Auto-Merge:** Any compound identified in the WAL but missing from the Parquet database is automatically re-processed and committed. This ensures a **0% data loss rate** across restarts.

---

## 4. Backup & Export Protocols

Beyond the local WAL, ChemoFilter provides three export formats available in the **"Export Analytics"** tab:

| Format | Purpose | Feature |
| :--- | :--- | :--- |
| **.CSV** | Universal Compatibility | Human-readable structural summary. |
| **.JSON** | Deep Integration | Full nested ADMET profile for Tier 1–9. |
| **.SMI** | Structural Library | Pure SMILES strings for docking in external tools. |

---

## 5. Security of Backups

*   **Offline-First:** All logs and backups stay on the user's machines.
*   **Encryption:** (Planned for Phase 4) Integration of the `cryptography` library to encrypt the Parquet database using a user-provided master password.
*   **Hash Integrity:** Every 1,000 writes, the system generates a checksum to verify that the Parquet database has not been corrupted at the disk level.

---

## 6. Maintenance Checklist (for System Admins)

*   **WAL Pruning:** After a successful Parquet commit, the `compounds_wal.jsonl` file is cleared to prevent unbounded growth.
*   **Schema Evolution:** If a new engine tier is added (e.g., Tier 11), the `reconcile_schema()` function in `data_engine.py` automatically updates existing Parquet files to include the new columns as null values.
