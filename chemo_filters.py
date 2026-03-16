
import math
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, AllChem, DataStructs, Crippen, Fragments
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
from rdkit.Chem.Scaffolds import MurckoScaffold

# -----------------------------------------------------------------------------
# 1. STRUCTURE VALIDATION & INTEGRITY
# -----------------------------------------------------------------------------

def is_valid_structure(mol):
    return mol is not None

def check_atom_valence(mol):
    if mol is None: return False
    try:
        mol.UpdatePropertyCache(strict=True)
        return True
    except:
        return False

def detect_disconnected_structure(mol):
    if mol is None: return False
    return len(Chem.GetMolFrags(mol)) > 1

def detect_abnormal_bonds(mol):
    if mol is None: return False
    for bond in mol.GetBonds():
        if bond.GetBondTypeAsDouble() > 3.0:
            return True
    return False

def detect_rings(mol):
    if mol is None: return False
    return mol.GetRingInfo().NumRings() > 0

def detect_aromatic_rings(mol):
    if mol is None: return False
    return rdMolDescriptors.CalcNumAromaticRings(mol) > 0

def detect_heteroatoms(mol):
    if mol is None: return False
    return rdMolDescriptors.CalcNumHeteroatoms(mol) > 0

def atom_diversity_check(mol):
    if mol is None: return 0
    return len(set(a.GetSymbol() for a in mol.GetAtoms()))

def structure_symmetry_check(mol):
    if mol is None: return 0.0
    ranks = list(Chem.CanonicalRankAtoms(mol, breakTies=False))
    if not ranks: return 0.0
    num_unique_ranks = len(set(ranks))
    num_atoms = mol.GetNumAtoms()
    if num_atoms == 0: return 0.0
    return 1.0 - (num_unique_ranks / num_atoms)

def molecule_normalization_test(mol):
    if mol is None: return False
    try:
        Chem.MolToSmiles(mol, isomericSmiles=True, canonical=True)
        return True
    except:
        return False

def check_formal_charge(mol):
    if mol is None: return 0
    return Chem.GetFormalCharge(mol)

def is_highly_charged(mol, threshold=2):
    return abs(check_formal_charge(mol)) > threshold

def has_chiral_centers(mol):
    if mol is None: return False
    return len(Chem.FindMolChiralCenters(mol, includeUnassigned=True)) > 0

def get_murcko_scaffold_heavy_atoms(mol):
    if mol is None: return 0
    try:
        scaf = MurckoScaffold.GetScaffoldForMol(mol)
        return scaf.GetNumHeavyAtoms()
    except:
        return 0

def check_inchi_generation(mol):
    if mol is None: return False
    try:
        Chem.MolToInchi(mol)
        return True
    except:
        return False

def get_atom_distribution(mol):
    if mol is None: return {}
    atoms = [a.GetSymbol() for a in mol.GetAtoms()]
    total = len(atoms)
    if total == 0: return {}
    dist = {}
    for sym in set(atoms):
        dist[f"ratio_{sym.lower()}"] = atoms.count(sym) / total
    return dist

def detect_unusual_valency(mol):
    if mol is None: return False
    # Typical valencies
    typical = {'H': [1], 'C': [4], 'N': [3, 4], 'O': [2], 'F': [1], 'P': [3, 5], 'S': [2, 4, 6], 'Cl': [1], 'Br': [1], 'I': [1]}
    for atom in mol.GetAtoms():
        sym = atom.GetSymbol()
        if sym in typical:
            v = atom.GetExplicitValence() + atom.GetImplicitValence()
            if v not in typical[sym]:
                return True
    return False

def get_topology_stats(mol):
    if mol is None: return {}
    ring_info = mol.GetRingInfo()
    nr = ring_info.NumRings()
    
    # Bridgehead atoms
    bridgeheads = 0
    spiro = 0
    for i in range(mol.GetNumAtoms()):
        if ring_info.NumAtomRings(i) > 2: bridgeheads += 1
        if ring_info.NumAtomRings(i) == 2: spiro += 1 # simplistic but often true for spiro in small mols
    
    return {
        "bridgehead_count": bridgeheads,
        "spiro_count": spiro,
        "ring_complexity": nr * (bridgeheads + 1)
    }

# -----------------------------------------------------------------------------
# 2. PROPERTY FILTERS (Massive RDKit Descriptors)
# -----------------------------------------------------------------------------

def get_all_descriptors(mol):
    if mol is None: return {}
    results = {}
    for name, func in Descriptors.descList:
        try:
            results[name] = func(mol)
        except:
            results[name] = 0.0
    return results

def get_physchem_props(mol):
    if mol is None: return {}
    return {
        "mw": Descriptors.MolWt(mol),
        "logp": Crippen.MolLogP(mol),
        "mr": Crippen.MolMR(mol),
        "tpsa": Descriptors.TPSA(mol),
        "hbd": rdMolDescriptors.CalcNumHBD(mol),
        "hba": rdMolDescriptors.CalcNumHBA(mol),
        "rot_bonds": rdMolDescriptors.CalcNumRotatableBonds(mol),
        "rings": rdMolDescriptors.CalcNumRings(mol),
        "aro_rings": rdMolDescriptors.CalcNumAromaticRings(mol),
        "het_rings": rdMolDescriptors.CalcNumHeterocyclicRings(mol),
        "heavy_atoms": mol.GetNumHeavyAtoms(),
        "total_atoms": mol.GetNumAtoms(onlyExplicit=False),
        "fsp3": rdMolDescriptors.CalcFractionCSP3(mol),
        "formal_charge": Chem.GetFormalCharge(mol),
        "complexity": Descriptors.BertzCT(mol),
        "labute_asa": rdMolDescriptors.CalcLabuteASA(mol),
        "hall_kier_alpha": Descriptors.HallKierAlpha(mol),
    }

def get_bond_density(mol):
    if mol is None: return 0.0
    nb = mol.GetNumBonds()
    na = mol.GetNumHeavyAtoms()
    return nb / na if na > 0 else 0.0

def get_heteroatom_ratio(mol):
    if mol is None: return 0.0
    h_atoms = rdMolDescriptors.CalcNumHeteroatoms(mol)
    total = mol.GetNumHeavyAtoms()
    return h_atoms / total if total > 0 else 0.0

def get_structural_flexibility(mol):
    if mol is None: return 0.0
    rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    heavy = mol.GetNumHeavyAtoms()
    return rot / heavy if heavy > 0 else 0.0

def estimate_steric_crowding(mol):
    if mol is None: return 0.0
    # Simplistic: Ratio of branched atoms to total heavy atoms
    branched = 0
    for atom in mol.GetAtoms():
        if atom.GetDegree() > 2:
            branched += 1
    return branched / mol.GetNumHeavyAtoms() if mol.GetNumHeavyAtoms() > 0 else 0.0

def get_molecular_compactness(mol):
    if mol is None: return 0.0
    # Ratio of ASA to Volume (lower often means more spherical/compact)
    try:
        asa = rdMolDescriptors.CalcLabuteASA(mol)
        vol = AllChem.ComputeMolVolume(mol)
        if vol > 0: return asa / vol
    except:
        pass
    return 0.0

# -----------------------------------------------------------------------------
# 3. FUNCTIONAL GROUP FILTERS (100+ SMARTS)
# -----------------------------------------------------------------------------

FUNCTIONAL_GROUPS_SMARTS = {
    "alcohol": "[OX2H]",
    "phenol": "[OX2H][c1ccccc1]",
    "ether": "[OD2]([#6])[#6]",
    "aldehyde": "[CX3H1](=O)[#6]",
    "ketone": "[#6][CX3](=O)[#6]",
    "carboxylic_acid": "[CX3](=O)[OX2H1]",
    "ester": "[CX3](=O)[OX2H0][#6]",
    "amide": "[NX3][CX3](=O)",
    "amide_primary": "[NX3H2][CX3](=O)",
    "amide_secondary": "[NX3H1]([#6])[CX3](=O)",
    "amine_primary": "[NX3H2][#6]",
    "amine_secondary": "[NX3H1]([#6])[#6]",
    "amine_tertiary": "[NX3]([#6])([#6])[#6]",
    "nitro": "[$([NX3](=O)=O),$([NX3+]([O-])=O)]",
    "sulfonamide": "[SX4](=O)(=O)[NX3]",
    "sulfonyl": "[SX4](=O)(=O)",
    "sulfide": "[#16X2]([#6])[#6]",
    "thiol": "[SX2H]",
    "phosphate": "P(=O)([OX2H,OX1-,[OX2]C])([OX2H,OX1-,[OX2]C])[OX2H,OX1-,[OX2]C]",
    "phosphonate": "P(=O)([#6])([OX2H,OX1-,[OX2]C])[OX2H,OX1-,[OX2]C]",
    "phosphite": "P([OX2H,OX1-,[OX2]C])([OX2H,OX1-,[OX2]C])[OX2H,OX1-,[OX2]C]",
    "halogen": "[F,Cl,Br,I]",
    "fluorine": "[F]",
    "chlorine": "[Cl]",
    "bromine": "[Br]",
    "iodine": "[I]",
    "nitrile": "[NX1]#[CX2]",
    "azide": "[N-2][N+]#N",
    "azo": "[NX2]=[NX2]",
    "epoxide": "C1OC1",
    "isocyanide": "[N+]#[C-]",
    "acid_halide": "[CX3](=[OX1])[F,Cl,Br,I]",
    "anhydride": "[CX3](=[OX1])[OX2][CX3](=[OX1])",
    "peroxide": "[OX2][OX2]",
    "hydrazine": "[NX3][NX3]",
    "hydroxylamine": "[NX3][OX2H]",
    "carbamate": "[NX3][CX3](=O)[OX2H0]",
    "urea": "[NX3][CX3](=O)[NX3]",
    "guanidine": "[NX3][CX3](=[NX2])[NX3]",
    "amidine": "[CX3](=[NX2])[NX3]",
    "oxime": "[CX3]=[NX2][OX2H]",
    "sulfone": "[#6][SX4](=O)(=O)[#6]",
    "sulfoxide": "[#6][SX3](=O)[#6]",
    "boronic_acid": "B([OX2H])[OX2H]",
    "silane": "[SiH4,SiH3R,SiH2R2,SiHR3,SiR4]",
    "alkyne": "[CX2]#[CX2]",
    "alkene": "[CX3]=[CX3]",
    "cyclopropane": "C1CC1",
    "cyclobutane": "C1CCC1",
    "cyclopentane": "C1CCCC1",
    "cyclohexane": "C1CCCCC1",
    "benzene": "c1ccccc1",
    "pyridine": "n1ccccc1",
    "pyrimidine": "n1cnccc1",
    "imidazole": "n1cncc1",
    "triazole": "[n,c]1[n,c][n,c][n,c][n,c]1",
    "tetrazole": "n1nnnn1",
    "indole": "c1ccc2[nH]ccc2c1",
    "quinoline": "c1ccc2ncccc2c1",
    "isoquinoline": "c1ccc2cnccc2c1",
    "furan": "c1ccoc1",
    "thiophene": "c1ccsc1",
    "pyrrole": "c1cc[nH]c1",
    "oxazole": "c1cnoc1",
    "thiazole": "c1cnsc1",
    "isoxazole": "c1con1",
    "isothiazole": "c1csn1",
    "morpholine": "[OX2]1CC[NX3]CC1",
    "piperidine": "[NX3]1CCCCC1",
    "piperazine": "[NX3]1CCNCC1",
    "tetrahydrofuran": "C1CCOC1",
    "tetrahydropyran": "C1CCOCC1",
    "pyrrolidine": "C1CNCC1",
    "diazo": "[CX3]=[N+]=[N-]",
    "perchlorate": "O=Cl(=O)(=O)[O-]",
    "nitroso": "[NX2]=O",
    "isocyanide": "[N+]#[C-]",
    "isocyanate": "[NX2]=[CX2]=O",
    "isothiocyanate": "[NX2]=[CX2]=S",
    "thiocyanide": "[SX2]C#[NX1]",
    "alkene_conjugated": "C=C-C=C",
    "acid_anhydride": "[CX3](=O)[OX2][CX3](=O)",
    "acyl_cyanide": "[CX3](=O)C#[NX1]",
    "beta_lactam": "N1C(=O)CC1",
    "beta_lactone": "O1C(=O)CC1",
    "strained_ring": "[r3,r4]",
    "phosphoric_acid": "P(=O)(O)(O)O",
    "phosphonic_acid": "P(=O)(O)(O)C",
    "sulfonic_acid": "S(=O)(=O)(O)C",
    "sulfinic_acid": "S(=O)(O)C",
    "sulfenic_acid": "S(O)C",
    "thiol_ester": "[CX3](=O)[SX2]",
    "thioketone": "[CX3]=[SX1]",
    "thioaldehyde": "[CX3H1]=[SX1]",
    "enamine": "[NX3][CX3]=[CX3]",
    "enol": "[OX2H][CX3]=[CX3]",
    "hydrazone": "[NX3][NX2]=[CX3]",
    "hydrazone": "[NX3][NX2]=[CX3]",
    "hydroxyl_amine": "[NX3][OX2H]",
    "adamantane": "[C@]12C[C@@H]3C[C@H](C[C@@H](C1)C3)C2",
    "steroid_core": "C1CCC2C(C1)CCC3C2CCC4(C3CCC4)",
    "quinoline_core": "n1ccc2ccccc21",
    "isoquinoline_core": "c1ccc2cnccc2c1",
    "purine_core": "n1cnc2c1ncnc2",
    "pteridine_core": "n1cnc2c1ncn2", # simplistic
    "coumarin": "O=C1Oc2ccccc2C=C1",
    "chalcone": "O=C(C=Cc1ccccc1)c1ccccc1",
    "urea_cyclic": "N1C(=O)NCC1",
    "hydantoin": "O=C1NC(=O)NC1",
    "barbiturate": "O=C1NC(=O)NC(=O)C1",
}

def detect_functional_groups(mol):
    if mol is None: return {}
    results = {}
    for name, smarts in FUNCTIONAL_GROUPS_SMARTS.items():
        pat = Chem.MolFromSmarts(smarts)
        if pat:
            matches = mol.GetSubstructMatches(pat)
            results[f"fg_{name}"] = len(matches)
            results[f"has_{name}"] = len(matches) > 0
        else:
            results[f"fg_{name}"] = 0
            results[f"has_{name}"] = False
    return results

# -----------------------------------------------------------------------------
# 4. SIMILARITY & SCREENING
# -----------------------------------------------------------------------------

def compute_fingerprint(mol, radius=2, nBits=2048):
    if mol is None: return None
    return AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nBits)

def compute_similarity(mol1, mol2, radius=2, nBits=2048):
    fp1 = compute_fingerprint(mol1, radius, nBits)
    fp2 = compute_fingerprint(mol2, radius, nBits)
    if fp1 and fp2:
        return DataStructs.TanimotoSimilarity(fp1, fp2)
    return 0.0

def detect_near_duplicates(mol, dataset_mols, threshold=0.9):
    if not mol or not dataset_mols: return []
    fp = compute_fingerprint(mol)
    matches = []
    for other in dataset_mols:
        if other == mol: continue
        fp2 = compute_fingerprint(other)
        sim = DataStructs.TanimotoSimilarity(fp, fp2)
        if sim >= threshold:
            matches.append(sim)
    return matches

def get_scaffold_info(mol):
    if mol is None: return {}
    try:
        scaffold = MurckoScaffold.GetScaffoldForMol(mol)
        smi = Chem.MolToSmiles(scaffold)
        return {
            "scaffold_smiles": smi,
            "scaffold_heavy_atoms": scaffold.GetNumHeavyAtoms(),
            "scaffold_rings": scaffold.GetRingInfo().NumRings()
        }
    except:
        return {}

def identify_structural_motifs(mol):
    # Common motifs like Lipinski's drug-like motifs
    motifs = {
        "biphenyl": "c1ccccc1-c2ccccc2",
        "triphenyl": "c1ccccc1-c2cc(cc1)-c3ccccc3",
        "fused_rings": "[r4,r5,r6,r7]@[r4,r5,r6,r7]",
    }
    matches = []
    for name, smarts in motifs.items():
        pat = Chem.MolFromSmarts(smarts)
        if pat and mol.HasSubstructMatch(pat):
            matches.append(name)
    return matches

def check_catalog_match(mol, catalog_type):
    params = FilterCatalogParams()
    if catalog_type == "PAINS":
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    elif catalog_type == "BRENK":
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.BRENK)
    elif catalog_type == "NIH":
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.NIH)
    elif catalog_type == "ZINC":
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.ZINC)
    
    catalog = FilterCatalog(params)
    if mol is None: return False
    return not catalog.HasMatch(mol)

# -----------------------------------------------------------------------------
# 5. DATASET TOOLS
# -----------------------------------------------------------------------------

def detect_duplicates(smiles_list):
    seen = {}
    duplicates = []
    for i, smi in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smi)
        if mol:
            can_smi = Chem.MolToSmiles(mol, canonical=True)
            if can_smi in seen:
                duplicates.append({"index": i, "smiles": smi, "original": seen[can_smi]})
            else:
                seen[can_smi] = i
    return duplicates

def get_dataset_diversity(mol_list):
    if not mol_list or len(mol_list) < 2: return 1.0
    fps = [compute_fingerprint(m) for m in mol_list if m]
    if not fps: return 0.0
    
    # Sample similarity between pairs
    n = len(fps)
    if n > 50: # subset for performance
        import random
        indices = random.sample(range(n), 50)
        fps = [fps[i] for i in indices]
        n = 50
        
    sims = []
    for i in range(n):
        for j in range(i+1, n):
            sims.append(DataStructs.TanimotoSimilarity(fps[i], fps[j]))
    
    if not sims: return 1.0
    avg_sim = sum(sims) / len(sims)
    return 1.0 - avg_sim

# -----------------------------------------------------------------------------
# 6. MASTER WRAPPER
# -----------------------------------------------------------------------------

def run_all_chemo_tests(mol, ref_mol=None):
    if mol is None: return {}
    
    # Base structure tests
    results = {
        "valid": is_valid_structure(mol),
        "valence_ok": check_atom_valence(mol),
        "disconnected": detect_disconnected_structure(mol),
        "abnormal_bonds": detect_abnormal_bonds(mol),
        "has_rings": detect_rings(mol),
        "has_aromatic": detect_aromatic_rings(mol),
        "has_hetero": detect_heteroatoms(mol),
        "atom_diversity": atom_diversity_check(mol),
        "symmetry": structure_symmetry_check(mol),
        "normalized": molecule_normalization_test(mol),
        "inchi_ok": check_inchi_generation(mol),
        "highly_charged": is_highly_charged(mol),
        "chiral": has_chiral_centers(mol),
        "stereocenter_count": len(Chem.FindMolChiralCenters(mol, includeUnassigned=True)),
        "bond_density": get_bond_density(mol),
        "hetero_ratio": get_heteroatom_ratio(mol),
        "flexibility": get_structural_flexibility(mol),
        "crowding": estimate_steric_crowding(mol),
        "compactness": get_molecular_compactness(mol),
        "unusual_valency": detect_unusual_valency(mol),
    }
    
    # Topology & Distribution
    results.update(get_topology_stats(mol))
    results.update(get_atom_distribution(mol))
    
    # PhysChem Properties
    results.update(get_physchem_props(mol))
    
    # All RDKit Descriptors (approx 200)
    results.update(get_all_descriptors(mol))
    
    # Functional Groups (approx 60)
    results.update(detect_functional_groups(mol))
    
    # Quality Catalogs
    results["no_pains"] = check_catalog_match(mol, "PAINS")
    results["no_brenk"] = check_catalog_match(mol, "BRENK")
    results["no_nih"] = check_catalog_match(mol, "NIH")
    results["no_zinc"] = check_catalog_match(mol, "ZINC")
    
    # Combined rules
    results["lipinski"] = (results["mw"] <= 500 and results["logp"] <= 5 and 
                          results["hbd"] <= 5 and results["hba"] <= 10)
    
    results["veber"] = (results["rot_bonds"] <= 10 and results["tpsa"] <= 140)
    results["ghose"] = (160 <= results["mw"] <= 480 and -0.4 <= results["logp"] <= 5.6 and 
                        40 <= results["mr"] <= 130 and 20 <= results["heavy_atoms"] <= 70)
    
    results["qed"] = Descriptors.qed(mol)
    
    # Scaffolds & Motifs
    results.update(get_scaffold_info(mol))
    results["motifs"] = identify_structural_motifs(mol)
    
    # SA Score (Simplified)
    results["sa_score"] = 1.0 + (results["mw"]/100) + (results["rings"]*0.5) + (results["fsp3"]*2.0)
    results["sa_score"] = min(10.0, results["sa_score"])
    
    if ref_mol:
        results["similarity"] = compute_similarity(mol, ref_mol)
        results["near_duplicate"] = (results["similarity"] >= 0.9)
    else:
        results["similarity"] = 0.0
        results["near_duplicate"] = False
        
    return results
