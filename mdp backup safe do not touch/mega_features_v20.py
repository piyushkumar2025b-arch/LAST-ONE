
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, Crippen
import math

def atom_counts(mol):
    """Counts specifically for various atoms."""
    return {
        "F_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[F]"))),
        "Cl_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[Cl]"))),
        "Br_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[Br]"))),
        "I_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[I]"))),
        "S_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[S]"))),
        "P_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[P]"))),
        "B_Count": len(mol.GetSubstructMatches(Chem.MolFromSmarts("[B]"))),
    }

def ring_size_distribution(mol):
    """Detailed ring size analysis."""
    ri = mol.GetRingInfo()
    rings = ri.AtomRings()
    dist = {}
    for r in rings:
        sz = len(r)
        dist[f"Ring_{sz}"] = dist.get(f"Ring_{sz}", 0) + 1
    return dist

def pfizer_3_75_rule(lp, tp):
    """Pfizer 3/75 toxicity rule (LogP > 3 and TPSA < 75)."""
    if lp > 3 and tp < 75: return "High RisK (Tox)"
    return "Low Risk"

def gsk_4_400_rule(lp, mw):
    """GSK 4/400 ADMET rule (LogP < 4 and MW < 400)."""
    if lp < 4 and mw < 400: return "Good Profile"
    return "Caution"

def oprea_rule(mol):
    """Oprea's lead-likeness rule."""
    hbd = rdMolDescriptors.CalcNumHBD(mol)
    hba = rdMolDescriptors.CalcNumHBA(mol)
    mw = Descriptors.MolWt(mol)
    lp = Descriptors.MolLogP(mol)
    rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    rings = rdMolDescriptors.CalcNumRings(mol)
    
    v = 0
    if mw <= 450: v += 1
    if lp <= 4.5: v += 1
    if hbd <= 5: v += 1
    if hba <= 9: v += 1
    if rot <= 8: v += 1
    if rings <= 4: v += 1
    return f"{v}/6 Pass"

def congreve_rule_of_3(mol):
    """Fragment-likeness (Rule of 3)."""
    mw = Descriptors.MolWt(mol)
    lp = Descriptors.MolLogP(mol)
    hbd = rdMolDescriptors.CalcNumHBD(mol)
    hba = rdMolDescriptors.CalcNumHBA(mol)
    rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    
    if mw <= 300 and lp <= 3 and hbd <= 3 and hba <= 3 and rot <= 3:
        return "Fragment-Like ✅"
    return "Not Fragment-Like"

def veber_rule_ext(rot, tp):
    """Detailed Veber Rule Check."""
    if rot <= 10 and tp <= 140: return "Pass (Oral)"
    return "Poor Oral Bio"

def mddr_likeness(mol):
    """MDDR-like drugness (number of rings > 3, rot bonds > 6)."""
    rings = rdMolDescriptors.CalcNumRings(mol)
    rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    if rings >= 3 and rot >= 6: return "Drug-Like (MDDR)"
    return "Moderate"

def flexibility_index(mol):
    """Rotatable bonds / Heavy atoms."""
    rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    heavy = mol.GetNumHeavyAtoms()
    return round(rot / heavy, 3) if heavy > 0 else 0

def molar_refractivity(mol):
    """Estimated Molar Refractivity."""
    return round(Crippen.MolMR(mol), 2)

def shape_index_kappa1(mol):
    """Kappa 1 index."""
    try:
        return round(rdMolDescriptors.CalcKappa1(mol), 3)
    except: return 0

def shape_index_kappa2(mol):
    """Kappa 2 index."""
    try:
        return round(rdMolDescriptors.CalcKappa2(mol), 3)
    except: return 0

def labute_asa(mol):
    """Labute Approximate Surface Area."""
    try:
        return round(rdMolDescriptors.CalcLabuteASA(mol), 2)
    except: return 0

def hallucination_score(mol):
    """Hypothetical 'Drug-likeness' hallucination score (Unique/Intuitiive)."""
    return round(Descriptors.MolLogP(mol) * 1.5 + Descriptors.MolWt(mol) / 150, 2)

def phase_ii_alerts(mol):
    """Alerts for common Phase II conjugation sites."""
    gluc = "[OH,NH,SH,COOH]" # Glucuronidation
    sulf = "[OH,NH2]" # Sulfation
    hits = []
    if mol.HasSubstructMatch(Chem.MolFromSmarts(gluc)): hits.append("Glucuronidation")
    if mol.HasSubstructMatch(Chem.MolFromSmarts(sulf)): hits.append("Sulfation")
    return ", ".join(hits) if hits else "Stable"

def isomer_count_hint(mol):
    """Theoretical stereoisomer complexity."""
    centers = len(Chem.FindMolChiralCenters(mol, includeUnassigned=True))
    db = 0
    return 2 ** (centers + db)

def bbb_v2_index(lp, tp, mw):
    """LogBB estimate (Clark equation)."""
    # logBB = 0.152*logP - 0.0148*TPSA + 0.139
    return round(0.152 * lp - 0.0148 * tp + 0.139, 3)

def molecular_flexibility(mol):
    """Percent of rotatable bonds."""
    n_rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    n_heavy = mol.GetNumHeavyAtoms()
    return round((n_rot / n_heavy * 100), 1) if n_heavy > 0 else 0

def h_bond_donors_detailed(mol):
    """Counts NH and OH specifically."""
    nh = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[NH,NH2]")))
    oh = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[OH]")))
    return {"NH": nh, "OH": oh}

def arom_heavy_ratio(mol):
    """Aromatic atoms / Heavy atoms."""
    heavy = mol.GetNumHeavyAtoms()
    arom = sum(1 for a in mol.GetAtoms() if a.GetIsAromatic())
    return round(arom / heavy, 3) if heavy > 0 else 0

def halogen_ratio(mol):
    """Halogens / Heavy atoms."""
    heavy = mol.GetNumHeavyAtoms()
    hal = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[F,Cl,Br,I]")))
    return round(hal / heavy, 3) if heavy > 0 else 0

def cyp_2d6_alert(mol):
    """Basic nitrogen at ~5A from hydrophobic site (heuristic)."""
    basic_n = mol.HasSubstructMatch(Chem.MolFromSmarts("[NX3;H2,H1,H0;!$(N-C=O)]"))
    if basic_n and Descriptors.MolLogP(mol) > 2.5: return "Likely Substrate"
    return "Low Risk"

def pka_acid_estimate(mol):
    """Heuristic pKa for common acids."""
    if mol.HasSubstructMatch(Chem.MolFromSmarts("C(=O)O")): return "~4-5 (Carboxyl)"
    if mol.HasSubstructMatch(Chem.MolFromSmarts("S(=O)(=O)O")): return "~1-2 (Sulfonic)"
    if mol.HasSubstructMatch(Chem.MolFromSmarts("Oc1ccccc1")): return "~9-10 (Phenol)"
    return ">12 (Neutral)"

def pka_base_estimate(mol):
    """Heuristic pKa for common bases."""
    if mol.HasSubstructMatch(Chem.MolFromSmarts("[NX4+]")): return ">11 (Quat)"
    if mol.HasSubstructMatch(Chem.MolFromSmarts("[NX3;H2,H1;!$(N-C=O)]")): return "~9-10 (Aliphatic)"
    if mol.HasSubstructMatch(Chem.MolFromSmarts("n1ccccc1")): return "~5 (Pyridine)"
    return "<2 (Weak)"

def hlia_prediction(tp):
    """High Liver Internal Accumulation (TPSA > 100 alert)."""
    if tp > 100: return "Elevated Risk"
    return "Standard"

def pka_gap(mol):
    """Potential for zwitterion formation."""
    acid = mol.HasSubstructMatch(Chem.MolFromSmarts("[CX3](=O)[OX2H1]"))
    base = mol.HasSubstructMatch(Chem.MolFromSmarts("[NX3;H2,H1,H0;!$(N-C=O)]"))
    if acid and base: return "Zwitterionic potential"
    return "Single/None"

def mol_volume(mol):
    """Molecular volume estimate."""
    return round(rdMolDescriptors.CalcLabuteASA(mol) * 0.8, 1)

def polarizability_estimate(mol):
    """Atomic refractivities heuristic."""
    return round(Crippen.MolMR(mol) / 2.5, 2)

def tpsa_per_heavy(mol, tp):
    """TPSA normalized by atom count."""
    h = mol.GetNumHeavyAtoms()
    return round(tp / h, 2) if h > 0 else 0

def bridgehead_complexity(mol):
    """Count of bridgehead atoms."""
    return rdMolDescriptors.CalcNumBridgeheadAtoms(mol)

def spiro_complexity(mol):
    """Count of spiro atoms."""
    return rdMolDescriptors.CalcNumSpiroAtoms(mol)

def sterics_index(mol):
    """Heavy atoms in branch points."""
    p = Chem.MolFromSmarts("[CX4](C)(C)(C)C") # Tert-butyl like
    return len(mol.GetSubstructMatches(p))

def heteroatom_ratio(mol):
    """Non-carbon atoms / Heavy atoms."""
    heavy = mol.GetNumHeavyAtoms()
    c = sum(1 for a in mol.GetAtoms() if a.GetSymbol()=="C")
    return round((heavy - c) / heavy, 3) if heavy > 0 else 0

def solubility_improvement_hint(lp):
    """Strategy to fix LogP."""
    if lp > 5: return "Add Hydroxyl/Amine"
    if lp < 0: return "Add Alkyl/Cyclohexyl"
    return "Balanced"

def metabolic_half_life_score(mol):
    """Structural complexity vs metabolic sites."""
    sites = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[CH3,CH2,CH]")))
    if sites > 10: return "Potential Short t1/2"
    return "Extended t1/2 likely"

def surface_roughness(mol):
    """Kappa3 index as proxy for branching/roughness."""
    try:
        return round(rdMolDescriptors.CalcKappa3(mol), 3)
    except: return 0

def ip_originality_score(sim):
    """100 - Tanimoto similarity to reference."""
    return round(100 * (1 - sim), 1)

def rule_of_5_ext(mol):
    """Classic Lipinski with warnings."""
    mw = Descriptors.MolWt(mol)
    lp = Descriptors.MolLogP(mol)
    hbd = rdMolDescriptors.CalcNumHBD(mol)
    hba = rdMolDescriptors.CalcNumHBA(mol)
    
    v = 0
    if mw > 500: v += 1
    if lp > 5: v += 1
    if hbd > 5: v += 1
    if hba > 10: v += 1
    return f"{4-v}/4"

def ghose_v2(lp, mw, h, refr):
    """Extended Ghose Check."""
    if (160 <= mw <= 480) and (-0.4 <= lp <= 5.6) and (20 <= h <= 70) and (40 <= refr <= 130):
        return "Pass"
    return "Fail"

def egan_v2(lp, tp):
    """Extended Egan Check."""
    if lp <= 5.88 and tp <= 131.6: return "Pass"
    return "Fail"

def covalent_danger_zone(mol):
    """Alert for highly reactive unwanted chemicals."""
    danger = ["[Cl,Br,I][C,S]", "[P,S][Cl,Br,I]", "[N,O,S]N=O", "C1CO1"]
    for d in danger:
        if mol.HasSubstructMatch(Chem.MolFromSmarts(d)): return "DANGER: HIGH REACTIVITY"
    return "Safe"

def toxicity_structural_alerts(mol):
    """Count of alert fragments for toxicity."""
    alerts = ["c1ccccc1O", "c1ccccc1N", "S=C(N)N", "[N+](=O)[O-]"]
    c = 0
    for a in alerts:
        c += len(mol.GetSubstructMatches(Chem.MolFromSmarts(a)))
    return c

def saturation_index(fsp3):
    """Categorical saturation."""
    if fsp3 > 0.45: return "Aliphatic Heavy"
    return "Aromatic Heavy"

def nitrogen_saturation(mol):
    """Sp3 nitrogens / Total nitrogens."""
    n_all = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[N]")))
    n_sp3 = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[NX3;H2,H1,H0;!$(N-C=O);!$(N-c)]")))
    return round(n_sp3 / n_all * 100, 1) if n_all > 0 else 0

def polar_exposure(tp, mw):
    """TPSA / MW ratio."""
    return round(tp / mw * 100, 3)

def bbb_likelihood_cat(lp, tp):
    """BBB categories."""
    if lp > 2 and tp < 60: return "High"
    if lp > 1 and tp < 90: return "Moderate"
    return "Low"

def ligand_efficiency(qed, heavy):
    """QED / Heavy atom count."""
    return round(qed / heavy * 10, 3) if heavy > 0 else 0

def binding_hotspot_prediction(mol):
    """Count of H-bond points per surface area."""
    hbd = rdMolDescriptors.CalcNumHBD(mol)
    hba = rdMolDescriptors.CalcNumHBA(mol)
    sa = rdMolDescriptors.CalcLabuteASA(mol)
    return round((hbd + hba) / sa * 100, 2) if sa > 0 else 0

def metabolic_clipping_alert(mol):
    """Alert for terminal methyls or esters."""
    methyl = len(mol.GetSubstructMatches(Chem.MolFromSmarts("[CH3]")))
    ester = len(mol.GetSubstructMatches(Chem.MolFromSmarts("C(=O)OC")))
    if methyl > 3 or ester > 1: return "Potential Clipping"
    return "Stable"

def omni_score(mol, qed, sim):
    """Mega-Metric: Combined Score (Aesthetic/Intuitve)."""
    return round(qed * 50 + sim * 30 + Descriptors.FractionCSP3(mol) * 20, 1)

def get_all_mega_v20(mol, qed, sim):
    mw = Descriptors.MolWt(mol); lp = Descriptors.MolLogP(mol); tp = Descriptors.TPSA(mol)
    h = mol.GetNumHeavyAtoms(); rot = rdMolDescriptors.CalcNumRotatableBonds(mol)
    hbd = rdMolDescriptors.CalcNumHBD(mol); hba = rdMolDescriptors.CalcNumHBA(mol)
    refr = Crippen.MolMR(mol); fsp3 = Descriptors.FractionCSP3(mol)
    
    data = {
        "Rule_of_5_Ext": rule_of_5_ext(mol),
        "Ghose_v2": ghose_v2(lp, mw, h, refr),
        "Egan_v2": egan_v2(lp, tp),
        "Pfizer_3_75": pfizer_3_75_rule(lp, tp),
        "GSK_4_400": gsk_4_400_rule(lp, mw),
        "Oprea_6": oprea_rule(mol),
        "Congreve_R3": congreve_rule_of_3(mol),
        "Veber_Oral": veber_rule_ext(rot, tp),
        "MDDR_Like": mddr_likeness(mol),
        "Flex_Index": flexibility_index(mol),
        "Molar_Refractivity": refr,
        "Kappa1": shape_index_kappa1(mol),
        "Kappa2": shape_index_kappa2(mol),
        "Labute_ASA": labute_asa(mol),
        "Halluc_Score": hallucination_score(mol),
        "Phase_II": phase_ii_alerts(mol),
        "Isomer_Count": isomer_count_hint(mol),
        "LogBB_Est": bbb_v2_index(lp, tp, mw),
        "Arom_Heavy_Ratio": arom_heavy_ratio(mol),
        "Halogen_Ratio": halogen_ratio(mol),
        "CYP_2D6_Hint": cyp_2d6_alert(mol),
        "pKa_Acidic": pka_acid_estimate(mol),
        "pKa_Basic": pka_base_estimate(mol),
        "HLIA_Risk": hlia_prediction(tp),
        "Zwitterion": pka_gap(mol),
        "Mol_Volume": mol_volume(mol),
        "Polarizability": polarizability_estimate(mol),
        "TPSA_per_Heavy": tpsa_per_heavy(mol, tp),
        "Bridgehead_Count": bridgehead_complexity(mol),
        "Spiro_Count": spiro_complexity(mol),
        "Sterics_Tert_Butyl": sterics_index(mol),
        "Heteroatom_Ratio": heteroatom_ratio(mol),
        "Sol_Improvement": solubility_improvement_hint(lp),
        "Metab_HalfLife": metabolic_half_life_score(mol),
        "Kappa3_Roughness": surface_roughness(mol),
        "IP_Originality": ip_originality_score(sim),
        "React_Danger": covalent_danger_zone(mol),
        "Tox_Alerts_Count": toxicity_structural_alerts(mol),
        "Sat_Cat": saturation_index(fsp3),
        "Nitrogen_Sat": nitrogen_saturation(mol),
        "Polar_Exposure": polar_exposure(tp, mw),
        "BBB_Likelihood": bbb_likelihood_cat(lp, tp),
        "Ligand_Efficiency": ligand_efficiency(qed, h),
        "Hotspot_Density": binding_hotspot_prediction(mol),
        "Clipping_Alert": metabolic_clipping_alert(mol),
        "Omni_Score": omni_score(mol, qed, sim)
    }
    data.update(atom_counts(mol))
    data.update(ring_size_distribution(mol))
    return data
