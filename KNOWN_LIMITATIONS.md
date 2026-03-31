# ⬡ ChemoFilter: Algorithmic Limitations

To maintain scientific integrity, an enterprise drug-discovery system must explicitly define what it **CAN** do and what it **CANNOT** do.

This file outlines the constraints of the Phase 1 topological baseline.

---

## 1. No "In Vivo" Systemic Profiling
The Lipinski rule set (MW < 500, LogP < 5) was generated historically from empirical failure rates. It guarantees a statistical probability of success, but it does NOT guarantee absolute biology.
*   **The Constraint:** Some of the most successful drugs in history explicitly violate everything on the dashboard (e.g. Lipitor (LogP: ~5.7, MW: 558), Macrolide antibiotics like Erythromycin (MW: 733)). 
*   These rule-breakers actively exploit secondary biological mechanics (transporter proteins / lipid-raft anchoring) that a topological 2D math model cannot physically see.

## 2. Protein-Ligand Disconnection
ChemoFilter (Phase 1) is a **Ligand-Only** profiling engine.
*   You cannot input a target receptor (e.g. the active site of the COVID-19 Main Protease).
*   The system scores drug-likeness based on baseline toxicity alarms and physiological solubility. It does NOT predict target affinity, IC50, or binding $\Delta G$ explicitly.

## 3. Stereocentre Flattening
The system does not inherently simulate chiral inversions in real-time biology (like the Thalidomide tragedy). It simply tallies the complexity via `Stereocenters: N` to calculate Synthesis Accessibility (`_sa_score`). D-enantiomers and L-enantiomers possessing wildly different toxicology profiles will score identical $O(1)$ Lead Scores.

## 4. Hardware Constraints
The Write-Ahead Log (.jsonl) buffers effectively against $O(N^2)$ memory fragmentation. However:
1.  **Browser Limits:** The `Plotly WebGL` scatter maps break at roughly 25,000 points. The native engine Python loops run perfectly infinitely, but the browser UI natively drops frames attempting to render infinite SVG scatter points.
2.  If scaling past 25,000 SMILES locally, users must disable the `fig_pca()` and `fig_boiled_egg()` visualizers entirely to prevent Streamlit rendering freezes.
