# ⬡ ChemoFilter: SMILES Formatting & Canonicalization Guide

**A Technical Manual for Standardizing Chemical Inputs**  
*Ensuring Data Integrity Across the 9-Tier Pipeline*

---

## 1. What is SMILES?

**SMILES (Simplified Molecular Input Line Entry System)** is the 1D string notation used by ChemoFilter to represent chemical structures. Every SMILES string is parsed through the RDKit C++ kernel in `data_engine.py` to generate the 2D/3D matrices needed for ADMET evaluation.

---

## 2. Input Requirements

To pass the Tier 1 (**Vanguard Core**) filter, your SMILES string must be valid based on the Daylight specification.

*   **Atoms:** Represented by [B, C, N, O, P, S, F, Cl, Br, I].
*   **Bonds:** Single (`-`), Double (`=`), Triple (`#`).
*   **Rings:** Indicated by numbers (e.g., `C1CCCCC1` for Cyclohexane).
*   **Aromaticity:** Lowercase atoms (e.g., `c1ccccc1` for Benzene).

---

## 3. The 3-Step Canonicalization Process

ChemoFilter does **not** rely on the raw string provided by the user. To prevent redundant API calls (and save on Anthropic LLM costs), the system executes a three-step **Canonicalization** routine before any math begins:

1.  **Sanitization:** The `RDKit.Chem.SanitizeMol` function checks for valency errors (e.g., a 5-bonded Carbon). Any molecule failing this is rejected by `app.py` with a **"Chemical Structure Error"** toast.
2.  **Kekulization:** To standardize aromatic representations, all ring systems are converted to their Kekulé form for deterministic mapping.
3.  **SMILES Canonicalization:** The string is converted to its unique, canonical representation.
    *   *User Input:* `C(C)OC(=O)C`
    *   *Canonical Output:* `CC(=O)OCC`
    *   *Benefit:* If the user enters the same drug twice in different formats, ChemoFilter recognizes the **SHA-256 hash** of the canonical string and returns the cached result instantly from `data/compounds.parquet`.

---

## 4. Handling Stereochemistry

ChemoFilter supports **chiral** SMILES using `@` and `@@` notations.

*   `@`: Anti-clockwise
*   `@@`: Clockwise

**Crucial Note:** Tier 9 (**Aether Primality**) will attempt to generate a 3D conformer based on the specified chirality. If the user provides a non-chiral SMILES for a chiral-capable molecule, the engine will pick the most energetically stable racemic form for its calculations.

---

## 5. Common Pitfalls & "Invalid Molecule" Flags

The engine will throw a "Structure Liability" alert if it detects:

*   **Disconnected Fragments:** Strings like `C1CCC.C1CCC` indicate a mixture. ChemoFilter will either fail or only process the largest fragment (configured in `chemo_filters.py`).
*   **Hyper-Valency:** `CC(=O)=O` (Carbon with 5 bonds) will trigger an immediate UI crash-protection state.
*   **Non-Physical Elements:** Elements like Xenon or Uranium are theoretically supported but will generate "N/A" for most ADMET parameters based on the current RDKit fragment library.

---

## 6. Pro-Tip: PubChem Linkage

If you do not know the SMILES string for a drug (e.g., Aspirin), you can enter the **PubChem CID** or simply the name into the "Web Search" sidebar tab. ChemoFilter will use `api_integrations.py` to fetch the canonical SMILES string from the PubChem REST API and prepopulate the input field for you.
