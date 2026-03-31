# ⬡ ChemoFilter: SMILES String Sanity Check

**Common "Impossible" Molecules and Chemical "Edge Cases"**  
*The "Sanitization Library" Behind Tier 1 (Vanguard Core)*

---

## 1. Executive Overview

Not all SMILES strings are chemically valid. A string may be syntactically correct (e.g., `C1CC1`) but non-physical (e.g., `CCCCC=N=C1`). **ChemoFilter** uses the RDKit C++ kernel to "Sanitize" every user input before it reaches the 9-Tier Processing Engine.

---

## 2. Common Sanity Failures (Structure Liabilities)

If a SMILES fails sanitization, the **"Vanguard Core"** throws a **"Structure Liability Alert"**:

1.  **Hyper-Valency:** A carbon with 5 or more bonds (e.g., `C(=C)(=C)(=C)C`). **Impossible.**
2.  **Disconnected Fragments:** A string that is actually two separate molecules (e.g., `C1CCCCC1.CC(O)C`). **Rejected.** (ChemoFilter only processes the largest fragment).
3.  **Non-Aromatic Rings:** A ring system that specifies aromaticity (lowercase atoms) but is not theoretically aromatic (e.g., `c1cccc1`—Cyclobutadiene). **Rejected as "Kekule Error."**

---

## 3. The 3-Step "Auto-Correction" Sequence

ChemoFilter attempts to fix minor issues before rejecting a lead:

*   **Step 1: Protonation.** If the SMILES is missing Hydrogens, Tier 1 uses `AddHs()` to fill the valence shell.
*   **Step 2: Canonicalization.** If two SMILES are different versions of the same drug, Tier 1 canonicalizes them to a single **SHA-256 hash**.
*   **Step 3: Salt Stripping.** If a user provides a drug with a salt (e.g., `CC(O)C.[Cl-]`), the **"Salts-Stripper"** module removes the Cl- to analyze only the active pharmacological component.

---

## 4. Handling "Unknown Atoms" ($*$)

Sometimes researchers want to test a **"Markush Structure"**—a scaffold with an unknown group ($*$).

| SMILES Flag | ChemoFilter Response | Scientific Outcome |
| :--- | :--- | :--- |
| **`C1CCC(*)CC1`** | **Rejected.** | Tier 1 requires an explicit atom (e.g., $N$) to calculate math. |
| **`C1=CC=C(C=C1)[He]`** | **Flagged.** | Helium atoms are supported but will return **"N/A"** for ADMET. |

---

## 5. Visualizing Failures: The "Red-Center" Glow

The **3D Conformational Force-Field Explorer** tab includes a **"Sanity Mask"** where:

*   **Atomic Glow (Red):** The specific atom in the SMILES string that caused the valency or kekule error is highlighted.
*   **Value:** An instant prompt for a chemist to correct the SMILES input.

---

## 6. How to Extend This Logic

Phase 5 (Roadmap) includes a **"Markush Library Generator"** that can automatically expand an unknown group ($*$) into 1,000 common side-chains for batch screening in the **"Scaffold Hopper"** module.
