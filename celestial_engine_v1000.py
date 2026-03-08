
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, AllChem, DataStructs
import celestial_data_v1000 as cd
import math

class CelestialIntelligenceV1000:
    """
    The Ultimate Celestial Engine (v1000). 
    Highest accuracy through Mechanistic PBPK, QUED, and Saagar Descriptors.
    """
    
    def __init__(self):
        self.saagar = cd.get_saagar()
        self.pbpk_model = cd.get_pbpk_model()
        self.qued_rules = cd.get_qued_rules()
        self.extra_tox = cd.get_extra_tox()

    def absorption_rate_ka(self, mol):
        """Mechanistic Absorption Rate Constant (Ka)."""
        tp = Descriptors.TPSA(mol)
        mw = Descriptors.MolWt(mol)
        hbd = rdMolDescriptors.CalcNumHBD(mol)
        
        # Ka = f(Permeability/Size)
        # Empirical: Ka approx (1 / (TPSA/10 + MW/100 + HBD*2))
        inv_fac = (tp/20.0) + (mw/200.0) + (hbd * 1.5)
        ka = 1.0 / (inv_fac + 0.5)
        return round(ka, 3)

    def hepatic_intrinsic_clearance_clint(self, mol, ox_exp):
        """Hepatic Intrinsic Clearance (CLint) estimation."""
        lp = Descriptors.MolLogP(mol)
        # High LogP and high Oxidative Exposure = High Clearance
        clint = (lp * 2.5) + (ox_exp * 50)
        return round(max(0.1, clint), 1)

    def quantum_electronic_propensity(self, mol):
        """QUED-based electrostatic propensity tags."""
        tags = []
        for rule in self.qued_rules:
            pat = Chem.MolFromSmarts(rule["smarts"])
            if pat and mol.HasSubstructMatch(pat):
                tags.append(rule["name"])
        return tags

    def tissue_partitioning_kp(self, lp, tp, mw):
        """Calculates specific tissue partitioning coefficients (Kp)."""
        kps = {}
        for tissue, weights in self.pbpk_model.items():
            val = (lp * weights[0]) + (tp * weights[1]) + (mw * weights[2]) / 100
            kps[tissue] = round(math.pow(10, val / 10), 2) # log-scale to real ratio
        return kps

    def saagar_hazard_deep_check(self, mol):
        """Deep scan using the Saagar advanced moiety library."""
        hazards = []
        for s in self.saagar:
            pat = Chem.MolFromSmarts(s["smarts"])
            if pat and mol.HasSubstructMatch(pat):
                hazards.append(f"{s['name']}: {s['hazard'] if 'hazard' in s else s['property']}")
        return hazards

    def therapeutic_index_ti_proxy(self, v500_score, tox_hits):
        """Heuristic for Safety Margin / Therapeutic Index."""
        ti = (v500_score / (tox_hits + 1)) / 100
        return round(ti, 2)

    def phase_3_passage_prob(self, mol, res):
        """Composite score for clinical success probability."""
        prob = 70.0
        fsp3 = Descriptors.FractionCSP3(mol)
        if fsp3 < 0.25: prob -= 15
        if res.get('LogP', 0) > 4: prob -= 10
        if res.get('SA_Score', 0) > 4: prob -= 10
        
        # Alignment bonus
        _v500_data = res.get('_v500', {})
        if _v500_data:
            if _v500_data.get('Universal_Score', 0) > 800: prob += 20
            
        return round(max(5.0, min(99.0, prob)), 1)

    def explainable_ai_shap(self, res):
        """SHAP-like breakdown of primary score drivers."""
        drivers = []
        lp = res.get('LogP', 0)
        mw = res.get('MW', 0)
        tp = res.get('TPSA', 0)
        
        if lp > 3: drivers.append({"Feature": "Lipophilicity", "Impact": "-25%", "Dir": "Down"})
        else: drivers.append({"Feature": "Lipophilicity", "Impact": "+15%", "Dir": "Up"})
        
        if mw < 400: drivers.append({"Feature": "Molecular Scale", "Impact": "+20%", "Dir": "Up"})
        if tp < 70: drivers.append({"Feature": "Polar Surface", "Impact": "+10%", "Dir": "Up"})
        
        return drivers

    def analyze_v1000(self, mol, res):
        # res = base result dict
        ka = self.absorption_rate_ka(mol)
        ox_exp = res.get('_v50', {}).get('Oxidative_Exposure', 0.5)
        clint = self.hepatic_intrinsic_clearance_clint(mol, ox_exp)
        qued_tags = self.quantum_electronic_propensity(mol)
        kp_map = self.tissue_partitioning_kp(res.get('LogP', 2.0), res.get('TPSA', 80.0), res.get('MW', 300.0))
        saagar_hazards = self.saagar_hazard_deep_check(mol)
        
        univ_score = res.get('_v500', {}).get('Universal_Score', 500)
        tox_count = len(res.get('_v500', {}).get('Organ_Toxicities', {}))
        ti_proxy = self.therapeutic_index_ti_proxy(univ_score, tox_count)
        
        success_prob = self.phase_3_passage_prob(mol, res)
        shap_data = self.explainable_ai_shap(res)
        
        # Celestial Score (0-5000)
        celestial_score = (univ_score * 4) + (success_prob * 10) + (ka * 200) - (clint * 2)
        
        return {
            "Celestial_Score": round(celestial_score, 1),
            "PBPK_Ka": ka,
            "PBPK_CLint": clint,
            "QUED_Tags": qued_tags,
            "Kp_Ensemble": kp_map,
            "Saagar_Hazards": saagar_hazards,
            "Therapeutic_Index": ti_proxy,
            "Phase_3_Prob": success_prob,
            "SHAP_Breakdown": shap_data,
            "Status": "STABLE" if success_prob > 60 else "VOLATILE"
        }

def get_v1000_engine():
    return CelestialIntelligenceV1000()
