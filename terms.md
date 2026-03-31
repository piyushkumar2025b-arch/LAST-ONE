# ⬡ ChemoFilter: Comprehensive Scientific Glossary

An exhaustive deep-dive lexicography of the biological, physical, topological, and pharmacological metrics calculated and displayed within the ChemoFilter engine. Evaluators may reference this document to understand the underlying rationale behind every platform warning, alert, and continuous score.

---

## Ⅰ. Fundamental Topology & Physicochemistry

*   **SMILES (Simplified Molecular-Input Line-Entry System):** A specification in the form of a line notation for describing the structure of chemical species using short ASCII strings. The fundamental input vector for the entire platform.
*   **Molecular Weight (MW):** The mass of a molecule in Daltons. Compounds $>500$ Da suffer from increasingly poor intestinal permeability, as dictated by early Lipinski heuristics.
*   **LogP (Partition Coefficient):** The base-10 logarithm of the ratio of concentrations of an un-ionized compound between octanol (lipid phase) and water (aqueous phase). A vital measure of lipophilicity. An optimal drug must traverse lipid membranes (requires high LogP) while remaining soluble in blood plasma (requires low LogP).
*   **TPSA (Topological Polar Surface Area):** The surface sum over all polar atoms, primarily oxygen and nitrogen, including their attached hydrogen atoms. $TPSA > 140$ Å² predicts poor oral bioavailability; $TPSA < 90$ Å² is canonically required for Blood-Brain Barrier (BBB) penetration.
*   **Fsp3 (Fraction of sp3 Carbons):** The number of sp3 hybridized (tetrahedral) carbons divided by the total carbon count. Higher Fsp3 correlates heavily with out-of-plane 3D complexity. Flat, purely aromatic molecules (low Fsp3) often suffer from poor solubility and off-target toxicity.
*   **Bertz Complexity (BertzCT):** A topological index quantifying the complexity of a molecule based on symmetry and branching. Extremely high complexity often drastically reduces Synthetic Accessibility, making the drug economically unviable to manufacture.
*   **Rotatable Bonds:** Defined as any single non-ring bond, bound to a non-terminal non-hydrogen atom. Excessive flexibility ($>10$ bonds) decreases the probability of a molecule adopting a distinct receptor-binding conformation.
*   **Halogen Ratio:** The proportion of halogen atoms (F, Cl, Br, I) to the total heavy atom count. Often tracked to monitor synthetic lipophilicity injections vs. metabolic liability.

## Ⅱ. Pharmacokinetics & ADME 

*   **ADME:** Absorption, Distribution, Metabolism, and Excretion.
*   **BOILED-Egg Model (Brain Or IntestinaL EstimateD permeation method):** A foundational predictive model charting WLOGP against TPSA to concurrently estimate both Gastrointestinal (GI) absorption (the "White") and Blood-Brain Barrier (BBB) permeability (the "Yolk").
*   **Caco-2 Permeability (Papp):** An *in vitro* metric predicting human intestinal absorption by measuring how quickly a compound crosses a generic human epithelial colorectal adenocarcinoma cell monolayer.
*   **ESOL (Estimated Aqueous Solubility):** Predicted $log S$ evaluating how effectively the compound dissolves in water at physiological pH, critical for oral systemic delivery. Calculated directly from structural topology.
*   **P-gp (P-glycoprotein 1):** A critical transmembrane efflux pump. Compounds flagged as P-gp substrates are actively pumped out of cells (specifically back into the intestinal lumen or out of the brain), significantly reducing their intracellular efficacy.
*   **First-Pass Effect:** The fraction of a drug lost during the initial pass through the liver via the portal vein before reaching systemic circulation.

## Ⅲ. Toxicity & Liability Screening

*   **PAINS (Pan-Assay Interference Compounds):** Specific structural motifs (e.g., quinones, rhodanines, toxoflavins) that frequently react non-specifically (acting as redox cyclers or fluorescence quenchers). They generate persistent false positives in high-throughput biological screens and must be aggressively filtered.
*   **hERG Risk (Human Ether-a-go-go-Related Gene):** Evaluates the affinity of the molecule to bind to the hERG potassium ion channel in the heart myocardium. Blockage induces Long QT Syndrome, potentially leading to fatal cardiac arrhythmias (Torsades de Pointes).
*   **Genotoxicity / Mutagenicity (Ames Test Proxy):** Specialized substructure matching algorithms that scan for structural alerts (e.g., aromatic amines, epoxides) known to intercalate within or alkylate DNA, determining carcinogenic potential.
*   **DILI (Drug-Induced Liver Injury):** Predictive flags identifying idiosyncratic hepatotoxic combinations that typically fail drugs in costly Phase II/III human trials.
*   **Reactive Metabolites:** Flags for groups that, upon Cytochrome P450 oxidation, form electrophilic species (e.g., Michael Acceptors) capable of indiscriminately covalently binding to cellular proteins causing an immune response.
*   **Phospholipidosis:** The excessive accumulation of phospholipids within cellular lysosomes, frequently triggered by Cationic Amphiphilic Drugs (CADs).

## Ⅳ. Heuristic Rules, Efficiency Metrics & Scoring Models

*   **Lipinski's Rule of Five (Ro5):** The ubiquitous industry standard for oral drug-likeness. A compound is likely to have poor absorption if it violates $\ge 2$ of the following: $MW > 500$, $LogP > 5$, $HBD > 5$, $HBA > 10$.
*   **Veber Rules:** Enhances Lipinski by adding geometric flexibility constraints: $Rotatable Bonds \le 10$ and $TPSA \le 140$ Å².
*   **Ghose Filter:** Constrains acceptable ranges for $MW$ (160 to 480), $LogP$ (-0.4 to 5.6), Molar Refractivity (40 to 130), and total distinct atoms (20 to 70).
*   **Egan Filter:** Focuses heavily on passive permeability, establishing strict boundaries $TPSA \le 132$ Å² and $LogP \le 5.8$.
*   **Muegge Filter (Pharmacophore Point Filter):** Defines boundaries for lead-like regions primarily to eliminate compounds that are too small or overly lipophilic.
*   **CNS MPO (Central Nervous System Multiparameter Optimization):** An algorithm producing a score from 0-6 modeling the probability of effective BBB crossing. High scores require low MW, low LogP, low TPSA, and low HBD.
*   **Ligand Efficiency (LE):** Defines the binding free energy or pIC50 normalized *per heavy atom*. Prevents chemists from endlessly adding molecular weight just to drive up binding affinity. 
*   **Lipophilic Efficiency (LipE):** Defined as $pIC50 - LogP$. Measures how efficiently a molecule translates lipophilicity into target potency.
*   **QED (Quantitative Estimate of Drug-likeness):** A continuous desirability function (0.0 to 1.0) mathematically synthesizing MW, LogP, TPSA, alarms, and aromatic rings into a single score representing the overall "beauty" of the structure.
*   **SA Score (Synthetic Accessibility Score):** Penalizes rare structural fragments and extreme topological complexity. Graded 1 (trivial to synthesize) to 10 (virtually impossible to synthesize economically).
*   **Lead Score (ChemoFilter Proprietary):** A 0-100 composite index generated locally that heavily weights biological safety over raw geometry. Converts raw RDKit models into a simple triage grade (e.g., A+ Clinical, D- Toxic) for rapid executive decision making.
