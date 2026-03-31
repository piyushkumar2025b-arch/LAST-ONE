# ⬡ ChemoFilter: Comprehensive Glossary of Pharmacology & Cheminformatics

**Standardized Scientific Terms Used Across the Analytical Engine**  
*A Reference Manual for Scientists, Engineers, and Evaluators*

---

## 1. Physicochemical & ADMET Foundation

*   **ADMET:** An acronym for **A**bsorption, **D**istribution, **M**etabolism, **E**xcretion, and **T**oxicity. These factors determine the pharmacological profile and ultimate clinical success of a drug candidate.
*   **Lipinski’s Rule of Five (Ro5):** A rule of thumb to evaluate if a chemical compound with a certain pharmacological or biological activity has properties that would make it a likely orally active drug in humans. 
    *   *Constraints:* $MW < 500$, $LogP < 5$, $H$-bond donors $< 5$, $H$-bond acceptors $< 10$.
*   **LogP (Octanol-Water Partition Coefficient):** A measure of hydrophobicity. It informs on the drug's ability to cross lipid membranes.
*   **PSA / TPSA (Topological Polar Surface Area):** The sum of surfaces of polar atoms (usually Nitrogens and Oxygens) in a molecule. Correlates with passive transport through membranes, particularly the **Blood-Brain Barrier (BBB)**.

---

## 2. Structural & Topological Descriptors

*   **SMILES:** *Simplified Molecular Input Line Entry System*. A 1D string notation representing molecular structures.
*   **Murcko Scaffold:** The core ring structure of a molecule after removing all side chains. Crucial for understanding the "structural backbone" of a drug class.
*   **Fsp3 (Fraction of sp3 carbons):** The ratio of $sp^3$ hybridized carbons to total carbon count. Higher $Fsp^3$ is associated with increased solubility and 3D structural complexity, which often leads to better clinical outcomes.
*   **Rotatable Bonds (RotB):** A measure of molecular flexibility. Compounds with too many rotatable bonds ($>10$) often have poor oral bioavailability.

---

## 3. Toxicity & Safety Pharmacology

*   **hERG (human Ether-à-go-go-Related Gene):** A gene that codes for a potassium ion channel in the heart. Blocking this channel can lead to fatal cardiac arrhythmias. ChemoFilter predicts hERG blockage risk using structural alerts.
*   **PAINS (Pan-Assay Interference Compounds):** Chemical motifs that show activity in many different biochemical assays regardless of the target, leading to "false positive" results.
*   **CYP450 (Cytochrome P450):** A superfamily of enzymes primarily responsible for drug metabolism in the liver. ChemoFilter predicts if a compound will inhibit or be a substrate for key isoforms like **CYP3A4** or **CYP2D6**.

---

## 4. Advanced Cheminformatic Indices

*   **QED (Quantitative Estimate of Drug-likeness):** A 0.0 to 1.0 score based on the desirability functions of several physicochemical properties. It is a modern, continuous alternative to the binary Rule of Five.
*   **SA_Score (Synthetic Accessibility Score):** A 1.0 to 10.0 score where a low score indicates a compound is easy to synthesize, while a high score suggests significant synthetic difficulty.
*   **Tanimoto Coefficient:** A statistical measure used to calculate the similarity between two molecular fingerprints. Values range from 0.0 (completely different) to 1.0 (identical structure).
*   **ESOL (Estimated SOLubility):** An algorithmic method to predict aqueous solubility directly from molecular structure without needing experimental data.

---

## 5. Mathematical & Engineering Layer

*   **WAL (Write-Ahead Logging):** A technique for ensuring data integrity by recording changes in a log file (`compounds_wal.jsonl`) *before* committing them to the primary database (`compounds.parquet`).
*   **Parquet:** A columnar storage file format that allows for high-performance data retrieval and compression, used by ChemoFilter to handle large molecular datasets.
*   **Jittered Exponential Backoff:** An algorithm for retrying failed API requests (like those to PubChem or Anthropic) with increasing delays and randomized "jitter" to avoid triggering rate limits.

---

## 6. How to Use This Glossary

This glossary should be referenced whenever an evaluator encounters a term in the **40+ Analytical Tabs** of the ChemoFilter interface that they are unfamiliar with. For deeper mathematical derivations, please see [ALGORITHMS_AND_MATH.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/ALGORITHMS_AND_MATH.md).
