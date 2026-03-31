# ⬡ ChemoFilter: Peer-Reviewed Scientific Bibliography & Literature Base

The rigorous predictive limitations, ADMET boundaries, scoring models, and substructure algorithms instantiated within the **ChemoFilter platform** are directly derived from canonical peer-reviewed medicinal chemistry literature. 

Evaluators verifying the integrity of the platform's alerts and limits should reference these definitive empirical works.

---

## I. Bioavailability Constraints & Rule Filtering
These papers established the continuous physical boundaries for oral drug viability. The platform uses these studies directly to assign instant "PASS / FAIL" conditionals.

1.  **Lipinski, C. A., Lombardo, F., Dominy, B. W., & Feeney, P. J. (2001).** 
    _Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings._ Advanced Drug Delivery Reviews, 46(1-3), 3-26. 
    > **Platform Implementation (`chemo_filters.py`):** The indisputable foundation for oral drug-likeness. Explicitly hardcoded into the `ChemoScore` algorithm. Any molecule violating $\ge 2$ parameters ($MW > 500$, $LogP > 5$, $HBD > 5$, $HBA > 10$) triggers severe viability degradation warnings.

2.  **Veber, D. F., Johnson, S. R., Cheng, H. Y., Smith, B. R., Ward, K. W., & Kopple, K. D. (2002).**
    _Molecular properties that influence the oral bioavailability of drug candidates._ Journal of Medicinal Chemistry, 45(12), 2615-2623.
    > **Platform Implementation (`chemo_filters.py`):** Operates tightly in parallel with Lipinski. Directly establishes the mathematical flexibility limits: Bioavailability drastically decreases if `Rotatable Bonds > 10` or `TPSA > 140 Å²`.

3.  **Ghose, A. K., Viswanadhan, V. N., & Wendoloski, J. J. (1999).**
    _A knowledge-based approach in designing combinatorial or medicinal chemistry libraries for drug discovery. 1. A qualitative and quantitative characterization of known drug databases._ Journal of Combinatorial Chemistry, 1(1), 55-68.
    > **Platform Implementation (`chemo_filters.py`):** A far tighter bounding box than Lipinski. Excludes compounds if Molar Refractivity ($MR$) deviates past $[40, 130]$ or total distinct atoms fall entirely outside $[20, 70]$.

4.  **Egan, W. J., Merz, K. M., & Baldwin, J. J. (2000).**
    _Prediction of drug absorption using multivariate statistics._ Journal of Medicinal Chemistry, 43(21), 3867-3877.
    > **Platform Implementation (`chemo_filters.py`):** Utilizes Egan's specialized $LogP \le 5.8$ passive permeability parameter alongside TPSA restrictions to act as a secondary orthogonal filter against the base Lipinski score.

## II. Multi-Parameter Optimization & Desirability Functions
These papers moved the industry away from binary "pass/fail" limits and toward continuous gradient scoring systems.

5.  **Bickerton, G. R., Paolini, G. V., Besnard, J., Muresan, S., & Hopkins, A. L. (2012).** 
    _Quantifying the chemical beauty of drugs._ Nature Chemistry, 4(2), 90-98.
    > **Platform Implementation (`features_v15.py`):** One of ChemoFilter's central metrics. Serves as the continuous scalar desirability function **[QED]** derived natively through RDKit. Generated accurately from a composite function encompassing 8 distinct properties simultaneously.

6.  **Wager, T. T., Hou, X., Verhoest, P. R., & Villalobos, A. (2010).**
    _Moving beyond rules: the development of a central nervous system multiparameter optimization (CNS MPO) approach to enable alignment of druglike properties._ ACS Chemical Neuroscience, 1(6), 435-449.
    > **Platform Implementation (`mega_features_v20.py`):** Essential for evaluating psychotropic vs peripherally active drugs. Computes a localized `CNS MPO` score bounded $0-6$, strictly penalizing basic pKa limits, heavily lipophilic domains, and large molecular weights attempting to traverse the BBB.

7.  **Hopkins, A. L., Groom, C. R., & Alex, A. (2004).**
    _Ligand efficiency: a useful metric for lead selection._ Drug Discovery Today, 9(10), 430-431.
    > **Platform Implementation (`terminonlogy.py`):** Defines the strict concept of **Ligand Efficiency (LE)**. Prevents theoretical molecule bloat by defining potency functionally relative to the raw count of heavy atoms. 

## III. Tissue Penetration, Solubility & Toxicity
These sources direct the models explicitly predicting physical absorption dynamics and hazardous molecular alarms.

8.  **Daina, A., & Zoete, V. (2016).** 
    _A BOILED-Egg To Predict Gastrointestinal Absorption and Brain Penetration of Small Molecules._ ChemMedChem, 11(11), 1117-1121.
    > **Platform Implementation (`visualization.py`):** Functions as the undeniable mathematical framework for the platform's visual **BOILED-Egg ADMET mapping plot**. Plots theoretical absorption geometries concurrently estimating the GI 'White Region' and BBB 'Yolk Region' strictly localized on Cartesian WLOGP / TPSA planes.

9.  **Baell, J. B., & Holloway, G. A. (2010).** 
    _New substructure filters for removal of pan assay interference compounds (PAINS) from screening libraries._ Journal of Medicinal Chemistry, 53(7), 2719-2740.
    > **Platform Implementation (`features_v15.py`):** A vital safety layer. Local `FilterCatalog` lists execute natively against Baell's designated SMARTS patterns, specifically isolating reactive aggregators and redox cyclers to halt development dynamically.

10. **Delaney, J. S. (2004).**
    _ESOL: estimating aqueous solubility directly from molecular structure._ Journal of Chemical Information and Computer Sciences, 44(3), 1000-1005.
    > **Platform Implementation (`mega_features_v20.py`):** Coded logic to evaluate estimated aqueous solubility ($log S$) natively substituting traditional thermodynamics with proxy topological indices (aromatic proportion and heavy atom totals).

11. **Ertl, P., Rohde, B., & Selzer, P. (2000).**
    _Fast calculation of molecular polar surface area as a sum of fragment-based contributions and its application to the prediction of drug transport properties._ Journal of Medicinal Chemistry, 43(20), 3714-3717.
    > **Platform Implementation (`features_v15.py`):** The direct computational basis for the ubiquitous **Topological Polar Surface Area (TPSA)**, executing extremely swift partial 2D polar mapping computations.
