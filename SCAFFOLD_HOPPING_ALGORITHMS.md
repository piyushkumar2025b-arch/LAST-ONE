# ⬡ ChemoFilter: Scaffold Hopping & Core Replacement Algorithms

**The Mathematics of Navigating Chemical Space**  
*The Logic of the "Bioisostere Hopper" Module (Tier 5)*

---

## 1. Executive Overview

**Scaffold Hopping** is the process of identifying structurally distinct molecules that share the same biological activity. **ChemoFilter** uses structural fingerprints and local bioisosteric mappings to suggest high-probability "Core Replacements" for a lead.

---

## 2. Defining Scaffold Similarity ($S_{scaf}$)

ChemoFilter uses the **Murcko Scaffold** (the ring system and linkers) to identify the core of a molecule. Similarity between two scaffolds is measured via the **Tanimoto Index**:

$$S_{scaf} = \frac{c_{scaf}}{a_{scaf} + b_{scaf} - c_{scaf}}$$

*   **Logic:** $c_{scaf}$ is the intersection of bitvectors for the two scaffolds.
*   **Result:** A **"Scaffold Match"** is triggered if $S_{scaf} > 0.6$.

---

## 3. The 3-Step "Hopping" Sequence

When the user activates the "Scaffold Hopper" in the UI:

1.  **Core Extraction:** The system extracts the **Murcko Scaffold** ($C_1$) of the lead.
2.  **Bioisostere Selection:** The system queries the **Bioisostere Replacement Database** for a structurally distinct but bioisosteric core ($C_2$).
3.  **Result Construction:** The side-chains ($R_1, R_2$) from the original molecule are automatically attached to the new core ($C_2$).

---

## 4. Visualizing Hopping: The "Core Transition" 3D Map

The UI features a **"Scaffold Transition Table"** where:

*   **Original Core:** Rendered in solid neon-cyan.
*   **Target Core:** Rendered as a transparent ghost.
*   **Observation:** The chemist can see at a glance if their side-groups $OH$ and $NH_2$ physically overlap in 3D space with the new core.

---

## 5. Significance in Intellectual Property (IP)

A successful **Scaffold Hop** allows a chemist to bypass a patent by discovering a molecule that is structurally distinct ($S_{scaf} < 0.4$) but biologically identical. ChemoFilter enables this "Freedom to Operate" analysis by exploring new chemical spaces instantly.

---

## 6. How to Extend This Engine

Phase 4 Roadmap involves a **Generative SMILES-to-SMILES LSTM** that can "Predict" the most biologically active core for a given set of side-chains, rather than relying on a static database of bioisosteres.
