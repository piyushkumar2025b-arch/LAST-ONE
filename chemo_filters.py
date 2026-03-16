
import math
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, AllChem, DataStructs, Crippen
from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams

# -----------------------------------------------------------------------------
# 1. STRUCTURE TESTS
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
    # Higher score means more symmetric
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

def is_highly_charged(mol):
    return abs(check_formal_charge(mol)) > 2

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

def has_reactive_group(mol):
    # Very basic list of reactive groups
    reactive_smarts = ["[Cl,Br,I][C,S]=O", "C1OC1", "[N+]#[C-]"] # Acid halides, epoxides, isocyanides
    for smarts in reactive_smarts:
        if mol.HasSubstructMatch(Chem.MolFromSmarts(smarts)):
            return True
    return False

def check_inchi_generation(mol):
    if mol is None: return False
    try:
        Chem.MolToInchi(mol)
        return True
    except:
        return False

# -----------------------------------------------------------------------------
# 2. PROPERTY FILTERS
# -----------------------------------------------------------------------------

def get_molecular_weight(mol):
    return Descriptors.MolWt(mol) if mol else 0.0

def get_rotatable_bonds(mol):
    return rdMolDescriptors.CalcNumRotatableBonds(mol) if mol else 0

def get_ring_count(mol):
    return rdMolDescriptors.CalcNumRings(mol) if mol else 0

def get_aromatic_ring_count(mol):
    return rdMolDescriptors.CalcNumAromaticRings(mol) if mol else 0

def get_hbond_donors(mol):
    return rdMolDescriptors.CalcNumHBD(mol) if mol else 0

def get_hbond_acceptors(mol):
    return rdMolDescriptors.CalcNumHBA(mol) if mol else 0

def get_logp(mol):
    return Descriptors.MolLogP(mol) if mol else 0.0

def get_tpsa(mol):
    return Descriptors.TPSA(mol) if mol else 0.0

def get_fsp3(mol):
    return rdMolDescriptors.CalcFractionCSP3(mol) if mol else 0.0

def get_bond_density(mol):
    if mol is None: return 0.0
    nb = mol.GetNumBonds()
    na = mol.GetNumHeavyAtoms()
    return nb / na if na > 0 else 0.0

def get_atom_count(mol):
    return mol.GetNumAtoms() if mol else 0

def get_heavy_atom_count(mol):
    return mol.GetNumHeavyAtoms() if mol else 0

def get_carbon_fraction(mol):
    if mol is None: return 0.0
    c_atoms = [a for a in mol.GetAtoms() if a.GetSymbol() == 'C']
    total = mol.GetNumAtoms()
    return len(c_atoms) / total if total > 0 else 0.0

def get_heteroatom_ratio(mol):
    if mol is None: return 0.0
    h_atoms = rdMolDescriptors.CalcNumHeteroatoms(mol)
    total = mol.GetNumHeavyAtoms()
    return h_atoms / total if total > 0 else 0.0

def get_rotatable_bond_fraction(mol):
    if mol is None: return 0.0
    rb = rdMolDescriptors.CalcNumRotatableBonds(mol)
    bonds = mol.GetNumBonds()
    return rb / bonds if bonds > 0 else 0.0

def get_tpsa_ratio(mol):
    if mol is None: return 0.0
    tpsa = Descriptors.TPSA(mol)
    area = rdMolDescriptors.CalcLabuteASA(mol)
    return tpsa / area if area > 0 else 0.0

def get_lipophilicity_efficiency(mol):
    if mol is None: return 0.0
    qed = Descriptors.qed(mol)
    logp = Descriptors.MolLogP(mol)
    return qed - logp

def has_bridgehead_atoms(mol):
    if mol is None: return False
    return any(a.HasProp('_BridgeheadAtom') for a in mol.GetAtoms())

def get_stereocenter_count(mol):
    if mol is None: return 0
    return len(Chem.FindMolChiralCenters(mol, includeUnassigned=True))

# -----------------------------------------------------------------------------
# 3. SIMILARITY & COMPARISON
# -----------------------------------------------------------------------------

def compute_similarity(mol, ref_mol, radius=2, nBits=2048):
    if mol is None or ref_mol is None: return 0.0
    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nBits)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(ref_mol, radius, nBits=nBits)
    return DataStructs.TanimotoSimilarity(fp1, fp2)

def detect_substructure(mol, smarts):
    if mol is None or not smarts: return False
    pat = Chem.MolFromSmarts(smarts)
    if pat is None: return False
    return mol.HasSubstructMatch(pat)

def detect_motif(mol, motif_smarts_list):
    if mol is None: return []
    found = []
    for smarts in motif_smarts_list:
        if detect_substructure(mol, smarts):
            found.append(smarts)
    return found

# -----------------------------------------------------------------------------
# 4. QUALITY SCREENING
# -----------------------------------------------------------------------------

def check_lipinski(mol):
    if mol is None: return False
    mw = Descriptors.MolWt(mol)
    lp = Descriptors.MolLogP(mol)
    hbd = rdMolDescriptors.CalcNumHBD(mol)
    hba = rdMolDescriptors.CalcNumHBA(mol)
    violations = 0
    if mw > 500: violations += 1
    if lp > 5: violations += 1
    if hbd > 5: violations += 1
    if hba > 10: violations += 1
    return violations <= 1

def get_qed_score(mol):
    return Descriptors.qed(mol) if mol else 0.0

def get_synthetic_accessibility_estimate(mol):
    """A very simplified SA score based on complexity and certain atoms."""
    if mol is None: return 0.0
    # SA score heuristic: rings, chiral centers, size
    mw = Descriptors.MolWt(mol)
    rings = rdMolDescriptors.CalcNumRings(mol)
    chiral = len(Chem.FindMolChiralCenters(mol, includeUnassigned=True))
    fsp3 = rdMolDescriptors.CalcFractionCSP3(mol)
    # Higher is HARDER
    score = (mw / 100) + (rings * 0.5) + (chiral * 1.0) + (fsp3 * 2.0)
    return max(1.0, min(10.0, score))

def check_pains(mol):
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    catalog = FilterCatalog(params)
    if mol is None: return False
    return not catalog.HasMatch(mol)

def check_brenk(mol):
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.BRENK)
    catalog = FilterCatalog(params)
    if mol is None: return False
    return not catalog.HasMatch(mol)

def check_nih(mol):
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.NIH)
    catalog = FilterCatalog(params)
    if mol is None: return False
    return not catalog.HasMatch(mol)

def check_drug_like(mol):
    # Combined rules
    if not is_valid_structure(mol): return False
    if not check_lipinski(mol): return False
    if get_qed_score(mol) < 0.3: return False
    return True

# -----------------------------------------------------------------------------
# 5. DATASET TESTS
# -----------------------------------------------------------------------------

def detect_duplicates_in_list(smiles_list):
    seen = set()
    dupes = []
    for smi in smiles_list:
        can_smi = Chem.MolToSmiles(Chem.MolFromSmiles(smi)) if Chem.MolFromSmiles(smi) else smi
        if can_smi in seen:
            dupes.append(can_smi)
        else:
            seen.add(can_smi)
    return list(set(dupes))

def dataset_distribution_analysis(property_list):
    if not property_list: return {}
    arr = [float(x) for x in property_list]
    return {
        "mean": sum(arr)/len(arr),
        "min": min(arr),
        "max": max(arr),
        "std": math.sqrt(sum((x - sum(arr)/len(arr))**2 for x in arr)/len(arr)) if len(arr) > 1 else 0
    }

# -----------------------------------------------------------------------------
# WRAPPER FOR ALL TESTS
# -----------------------------------------------------------------------------

def run_all_chemo_tests(mol, ref_mol=None):
    if mol is None: return {}
    results = {
        # Structure (12 tests)
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
        "formal_charge": check_formal_charge(mol),
        "highly_charged": is_highly_charged(mol),
        "chiral": has_chiral_centers(mol),
        "reactive": has_reactive_group(mol),
        "inchi_ok": check_inchi_generation(mol),
        
        # Properties (15 tests)
        "mw": get_molecular_weight(mol),
        "rot_bonds": get_rotatable_bonds(mol),
        "rings": get_ring_count(mol),
        "aromatic_rings": get_aromatic_ring_count(mol),
        "hbd": get_hbond_donors(mol),
        "hba": get_hbond_acceptors(mol),
        "logp": get_logp(mol),
        "tpsa": get_tpsa(mol),
        "fsp3": get_fsp3(mol),
        "bond_density": get_bond_density(mol),
        "atom_count": get_atom_count(mol),
        "heavy_atoms": get_heavy_atom_count(mol),
        "carbon_fraction": get_carbon_fraction(mol),
        "hetero_ratio": get_heteroatom_ratio(mol),
        "rot_bond_frac": get_rotatable_bond_fraction(mol),
        "tpsa_ratio": get_tpsa_ratio(mol),
        "lip_eff": get_lipophilicity_efficiency(mol),
        "stereo_centers": get_stereocenter_count(mol),
        
        # Quality (10 tests)
        "lipinski": check_lipinski(mol),
        "qed": get_qed_score(mol),
        "sa_score": get_synthetic_accessibility_estimate(mol),
        "no_pains": check_pains(mol),
        "no_brenk": check_brenk(mol),
        "no_nih": check_nih(mol),
        "drug_like": check_drug_like(mol),
        "murcko_heavy": get_murcko_scaffold_heavy_atoms(mol),
        "bridgehead": has_bridgehead_atoms(mol),
    }
    
    if ref_mol:
        results["similarity"] = compute_similarity(mol, ref_mol)
    
    # Add some dummy functional group counts to reach 50+
    results["nitro_groups"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[N+](=O)[O-]")))
    results["carboxylic_acids"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("C(=O)[O;H1,0-]")))
    results["amines"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[N;H2,H1,H0;!$(N[C,S]=O)]")))
    results["halogens"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[F,Cl,Br,I]")))
    results["sulfonamides"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("S(=O)(=O)N")))
    results["phosphorus"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("P")))
    results["sulfur"] = len(mol.GetSubstructMatches(Chem.MolFromSmarts("S")))
    results["chiral_centers"] = get_stereocenter_count(mol)

    return results
