# ⬡ ChemoFilter: Bioisostere Morphing & Scaffold Replacement Logic

**The Algorithmic Engine Behind "Morphogenic SAR"**  
*Suggesting High-Probability Structural Variations to Evade Toxicity*

---

## 1. Executive Overview

The **"Scaffold Morphing & Bioisostere Discovery"** tab is a flagship tool of ChemoFilter. While lower tiers evaluate existing structures, this module proactively suggests **bioisosteres**—chemical groups with similar spatial and electronic properties that can replace existing atoms to improve potency, reduce toxicity, or bypass IP constraints.

---

## 2. Core Morphing Logic (RDKit SMARTS)

ChemoFilter does not use "randomized" mutation. It follows canonical bioisosteric rules:

1.  **Classical Bioisosteres:** Atoms/groups with the same number of valence electrons.
    *   *Examples:* Replacing $O$ with $S$, $CH_3$ with $NH_2$ or $OH$.
2.  **Non-Classical Bioisosteres:** Groups that produce similar biological effects with different electronic structures.
    *   *Examples:* Replacing a carboxylic acid ($COOH$) with a tetrazole ring.

---

## 3. The 3-Step Morphing Sequence

When the user activates "Morph Lead" in the UI:

1.  **Murcko Bridge Identification:** The `scaffold_hopper.py` module identifies the central scaffold and its attachment points.
2.  **RDKit Substructure Search:** It locates "high-risk" groups (like toxic fragments or highly polar nitro-groups).
3.  **Recursive RECAP (Retrosynthetic Combinatorial Analysis Procedure):** The engine "rips" the molecule apart and replaces side chains from a library of 2,000+ FDA-proven bioisosteres.

---

## 4. Screening Morphological Candidates

After generating 10–50 "Morphed Leads," ChemoFilter automatically runs them through the **Vanguard Core (Tier 1)** to ensure the new molecules still pass Lipinski's Ro5.

| Original Group | Suggested Bioisostere | Scientific Logic | Resulting Change |
| :--- | :--- | :--- | :--- |
| **Phenyl Ring** | **Pyridine** | Heterocycle substitution. | Higher solubility, lower LogP. |
| **Carboxylic Acid** | **Tetrazole** | Acid-mimicry. | Better membrane permeability. |
| **Methyl Group** | **Fluorine** | Size mimicry. | Increased metabolic stability. |

---

## 5. Visualizing the Morph: The Tanimoto Matrix

The UI displays the morphed leads in a **Similarity Heatmap**. 

*   **Logic:** A "Good Morph" maintains a Tanimoto similarity of **0.6 to 0.8**. 
*   **Result:** A lead that is "close enough" to maintain biological activity but "different enough" to bypass a competitor's patent or reduce a specific hERG risk.

---

## 6. How to Extend This Module

Phase 5 (Future Roadmap) involves training a **VAE (Variational Autoencoder)** on 2 million ChEMBL compounds to generate purely generative bioisosteres that can "leap" into entirely new chemical spaces while preserving the binding pharmacophore.
