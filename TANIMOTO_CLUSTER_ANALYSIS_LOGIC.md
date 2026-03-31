# ⬡ ChemoFilter: Tanimoto Cluster Analysis Logic

**The Science of Identifying Structural Families in Large Libraries**  
*The Hierarchical & K-Means Clustering of Morgan Fingerprints*

---

## 1. Executive Overview

In virtual screening, a "Diverse Library" is better than a "Redundant" one. **Tanimoto Cluster Analysis** (in `data_engine.py`) identifies groups of molecules with similar chemical scaffolds. This document details the mathematical logic for segmenting 1,000+ compounds into "Structural Families."

---

## 2. K-Means Clustering (BitVector Centroids)

For sets of $1,000+$ compounds:

1.  **BitVector Extraction:** For every molecule, the 2048-bit **Morgan Fingerprint (Radius 2)** is extracted.
2.  **Distance Metric:** Instead of Euclidean distance, the engine uses **Tanimoto Distance** ($1 - Sim$) to measure the gap between bitvectors.
3.  **Centroid Calculation:** The "Medoid" (The most representative molecule) in each cluster is identified as the **Scaffold Lead**.

---

## 3. Hierarchical Clustering (The Scaffold Tree)

For sets of $< 100$ compounds (e.g., the top 100 leads):

*   **Logic:** A bottom-up approach where the two most similar molecules are merged into a cluster, until a single "Tree" (Dendrogram) remains.
*   **Significance:** Users can see exactly which "Branch" of the structural tree a lead belongs to.

---

## 4. Visualizing Clusters: The "Analytical Dashboard"

The UI features a **Clustered Heatmap** where:

*   **Logic:** Columns and rows are re-ordered so that similar molecules are grouped together.
*   **Result:** Large "Blocks" of dark cyan indicate a cluster.
*   **Actionable Insight:** Identifying a "Potent Cluster" of 10 molecules allows the chemist to explore "Structural Tuning" within that scaffold family.

---

## 5. Identifying "Singlets" (Unique Leads)

A molecule that does not belong to any cluster is identified as a **"Singlet"**.

| Lead Type | Cluster Count | Scientific Outcome |
| :--- | :--- | :--- |
| **Family Lead** | $> 10$ | High confidence. A proven scaffold class. |
| **Singlet** | $1$ | **Highest Discovery Potential.** Potentially a novel mechanism of action or a new chemical space. |

---

## 6. How to Extend This Logic

Phase 5 Roadmap involves **GNN (Graph Neural Network) Embedding**, where the structural clusters are combined with biological $pIC_{50}$ values to identify "Potency-Clusters"—groups of molecules that are structurally different but share the same pharmacological effect.
