# ⬡ ChemoFilter: System Data Dictionary

When external users (e.g., Data Scientists) download a `.CSV` or `.JSON` dossier from the platform, they must understand the exact scalar boundaries, types, and definitions of the columns. 

This is the explicit map of the array schemas returned by the ChemoFilter processing loops.

---

### Core Identifiers
| Column Name | Data Type | Range/Format | Definition |
| :--- | :--- | :--- | :--- |
| **ID** | `String` | `Cpd-1`, `Cpd-2` | Deterministic array index string. |
| **SMILES** | `String` | ASCII | Simplified Molecular-Input Line-Entry System formulation. |
| **Cluster** | `String` | Category | Assigned based on structural size/similarity (`Target Lead`, `Reference`, `Oversized`, `Non-Organic`). |

### Main Target Viability
| Column Name | Data Type | Range/Format | Definition |
| :--- | :--- | :--- | :--- |
| **Grade** | `String` | `A`, `B`, `C`, `F` | Absolute viability grade based on Lipinski violations and toxicity. |
| **LeadScore** | `Float` | `0.0` - `100.0` | Comprehensive algorithmic rank weighting geometry vs toxicity. |
| **QED** | `Float` | `0.000` - `1.000` | Quantitative Estimate of Druglikeness (Bickerton equation). |
| **SA_Score** | `Float` | `1.0` - `10.0` | Synthetic Accessibility. 1 = Easy synthesis, 10 = Theoretically impossible. |

### Geometrical & Physical Coordinates
| Column Name | Data Type | Range/Format | Definition |
| :--- | :--- | :--- | :--- |
| **MW** | `Float` | Daltons | Molecular Weight constraint (Target: < 500). |
| **LogP** | `Float` | Typically `-4.0` to `9.0` | Octanol-Water partition. Higher = explicitly lipophilic/fat-soluble. |
| **tPSA** | `Float` | Angstroms² | Topological Polar Surface Area (Target oral: < 140). |
| **HBD** / **HBA** | `Integer` | `0` - `~20` | Hydrogen Bond Donors / Acceptors. (Target: < 5 don, < 10 acc). |
| **RotBonds** | `Integer` | `0` - `~50` | Rotatable bonds (Target: < 10). Excess causes ligand entropy penalties. |
| **Fsp3** | `Float` | `0.00` - `1.00` | Fraction of sp3-hybridized carbons. Indicates 3-Dimensional complexity. |

### Toxicological Alarms
| Column Name | Data Type | Range/Format | Definition |
| :--- | :--- | :--- | :--- |
| **PAINS** | `String/Bool` | `✅ Clean` or `⚠️ N` | Pan-Assay Interference Compound flag. Disqualifies molecules instantly. |
| **hERG** | `String` | `LOW`, `MEDIUM`, `HIGH`| Cardiac arrhythmia liability. Assessed via aromatic rings and basic nitrogen. |
| **Ames** | `String` | Category | Mutagenicity profile (e.g., "Likely Mutagen"). |
| **CYP_Hits** | `Integer` | `0` - `5` | Sum of Cytochrome P450 isoenzymes explicitly triggered by the scaffold. |

### Biological Boundaries
| Column Name | Data Type | Range/Format | Definition |
| :--- | :--- | :--- | :--- |
| **HIA** | `Bool/String` | `✅` or `❌` | Human Intestinal Absorption estimation via the BOILED-EGG parameters. |
| **BBB** | `Bool/String` | `✅` or `❌` | Blood-Brain Barrier permeation estimation. |
| **CNS_MPO** | `Integer` | `0` - `6` | Multiparameter optimization rating strictly for neuro-active target profiling. |
