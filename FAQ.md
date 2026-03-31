# ⬡ ChemoFilter: Frequently Asked Questions (FAQ)

A quick-reference guide answering the most common functional, scientific, and architectural questions regarding the platform.

---

### ❓ 1. Why did my compound receive a Lead Score of 0?
The **Lead Score** algorithm heavily prioritizes biological safety over theoretically perfect geometry. If your compound triggered a severe **PAINS alarm** (an assay interference compound) or exceeded critical limits known to induce **hERG toxicity** (cardiac arrhythmia), the `chemo_scoring.py` module drops the final viability grade to 0 (Grade F). The logic is that no amount of target affinity justifies advancing an inherently toxic structure to clinical trials.

### ❓ 2. Is my proprietary SMILES data sent to a cloud server?
**No.** All core structural mapping, RDKit processing, descriptor generation, and Parquet caching happen 100% locally on your machine. 
*Exception:* If you explicitly use the **🤖 Mechanistic Result Interpretation Engine** tab, the data matrix is serialized and sent to Anthropic (Claude) for evaluation. If your data is proprietary, simply do not enter an API key into `.streamlit/secrets.toml`, and the engine will remain entirely offline.

### ❓ 3. What does the "🚀 Demo Mode" button actually do?
Located on the landing page, clicking this button intercepts the manual input loop. It automatically feeds a string of five highly-researched, classical molecules (*Aspirin, Ibuprofen, Paracetamol, Caffeine, and Olanzapine*) into the parsing engine. This allows evaluators at the VIT MDP Open House to witness the platform generating hundreds of complex metrics without having to memorize or copy-paste SMILES strings.

### ❓ 4. What is the difference between "Vanguard Core" (Tier 1) and "Aether Primality" (Tier 9)?
ChemoFilter uses a tiered architecture to maintain UI speed:
*   **Tier 1** calculates the lightweight math: calculating mass (MW), counting basic Hydrogen Bonds (HBD/HBA), and executing the Lipinski boolean limits.
*   **Tier 9** calculates theoretical, heavy-compute algorithms requiring deep topological branching. By segregating the math, the UI can render instantly using Tier 1 data while Tier 9 calculates quietly in the background asynchronously.

### ❓ 5. Why are you using Parquet instead of CSV databases?
When analyzing thousands of molecules, continuous appending to a pandas DataFrame/CSV causes extreme memory fragmentation ($O(N^2)$ quadratic scaling). **FastParquet** allows the platform to write molecular vectors into independent column batches asynchronously—meaning evaluating 10,000 compounds takes the same exact RAM as 10 compounds.

### ❓ 6. What is the BOILED-EGG model?
The **B**rain **O**r **I**ntestina**L** **E**stimate**D** permeation method (Daina, 2016). It is the primary visual scatter-plot on the dashboard. It graphs lipophilicity (WLOGP) against polarity (TPSA). 
*   Compounds falling in the "White" region should be absorbed by the stomach. 
*   Compounds falling in the "Yolk" region are lipophilic enough to cross the Blood-Brain Barrier (BBB).

### ❓ 7. I uploaded a CSV, but it says "No smiles column found"?
The `chemo_io.py` script automatically scans uploaded `.csv` or `.xlsx` files for headers. Your column containing the chemical strings **must** be named `SMILES`, `smi`, or `structure` (case-insensitive) for the engine to grab the array.
