# ⬡ ChemoFilter: SAR Visualization & Analytical Matrices

**The Science of "Structure-Activity Relationship" (SAR) Graphics**  
*Understanding the Heatmaps, Clustering, and PCA Maps of the Dashboard*

---

## 1. Executive Overview

A key challenge in Cheminformatics is turning 100,000 statistical data points into a single "Aha!" moment for a scientist. The **Analytical Interface Suite** in `app.py` uses five primary visualization matrices to help users navigate the chemical multiverse of their results.

---

## 2. The Tanimoto Similarity Heatmap ($100 \times 100$)

When a user selects "Cluster View" for a library of leads:

*   **Logic:** The system calculates a full bitwise similarity matrix between every compound.
*   **Result:** A **Heatmap** where "hot" (dark cyan) cells indicate highly similar compounds ($Sim > 0.8$) and "cold" (black) cells indicate structural diversity.
*   **Scientific Value:** Identifies "Scaffold Families"—groups of molecules that likely share a common biological activity.

---

## 3. The PCA Projection Map (Principal Component Analysis)

ChemoFilter uses PCA to compress 200+ dimensions (MW, LogP, TPSA, Fsp3, etc.) into a 2D or 3D scatter plot.

*   **Logic:** The first two principal components ($PC1$, $PC2$) explain the most variance in the dataset.
*   **Result:** A dynamic **3D Scatter Plot** (Plotly-backed) where clusters of points indicate molecules with similar physical properties.
*   **Scientific Value:** Points that drift away from the main cluster are "outliers" (potential new drug classes or "chemical nonsense").

---

## 4. The BOILED-Egg Model (Brain & GI Mapping)

Named for its "White" and "Yolk" zones:

*   **Implementation:** Plotting **WLOGP** (Wildman-Crippen LogP) against **TPSA**.
*   **Yolk Zone:** High probability of crossing the Blood-Brain Barrier (BBB).
*   **White Zone:** High probability of Gastrointestinal (GI) absorption.
*   **Scientific Value:** A single plot that predicts the "Drug-Likeness" better than simple Ro5 filters.

---

## 5. The Scaffold Diversity "Sunburst" Chart

By extracting **Murcko Scaffolds**, ChemoFilter creates a hierarchical "Sunburst" chart:

1.  **Inner Ring:** Core Ring Systems (e.g., Indoles, Pyridines).
2.  **Outer Ring:** Specific side-chain modifications.
3.  **Scientific Value:** Instantly shows if a user's library is "Diverse" or if it is redundantly focused on a single structural motif.

---

## 6. The WebGL 3D Conformational Force-Field Explorer

Using **NGLView / Py3Dmol** (depending on the container environment), ChemoFilter maps 2D SMILES into 3D.

*   **Logic:** Execution of the **MMFF94** (Merck Molecular Force Field) to minimize energy conformers.
*   **Scientific Value:** Allows chemists to verify if a molecule is "Flat" (low Fsp3) or "Bulky" (high Fsp3), which is crucial for successful clinical outcomes.
