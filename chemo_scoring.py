
def calculate_chemo_score(results, weights=None):
    """
    results: dict from run_all_chemo_tests
    weights: dict with weights for different categories
    Returns a dictionary (Package) with:
      - score: float (0-100)
      - grade: str (A+, A, B, C, F)
      - components: dict (breakdown of scores)
    """
    if not results: return {"score": 0.0, "grade": "F", "components": {}}
    
    if weights is None:
        weights = {
            "structure": 0.20,
            "physchem": 0.25,
            "drug_likeness": 0.20,
            "safety": 0.25,
            "complexity": 0.10
        }
        
    # 1. Structure Quality (0-1)
    s_score = 0.0
    s_factors = [
        results.get("valid", False),
        results.get("valence_ok", False),
        not results.get("disconnected", True),
        not results.get("highly_charged", True),
        results.get("normalized", False),
        results.get("inchi_ok", False)
    ]
    s_score = sum(1.0 for f in s_factors if f) / len(s_factors)
    
    # 2. PhysChem / Drug-Likeness (0-1)
    # We use a weighted combination of Lipinski, Veber, and QED
    qed = results.get("qed", 0.0)
    lipinski = 1.0 if results.get("lipinski") else 0.0
    veber = 1.0 if results.get("veber") else 0.0
    p_score = (qed * 0.4) + (lipinski * 0.4) + (veber * 0.2)
    
    # 3. Property Compliance (specifically LOGP and MW)
    # Target LogP 1.5, MW 350
    mw = results.get("mw", 0)
    lp = results.get("logp", 0)
    mw_score = 1.0 - min(1.0, abs(mw - 350) / 350)
    lp_score = 1.0 - min(1.0, abs(lp - 1.5) / 4.0)
    prop_score = (mw_score * 0.5) + (lp_score * 0.5)
    
    # 4. Safety (0-1)
    # PAINS, NIH, BRENK
    safe_score = 0.0
    pains = 1.0 if results.get("no_pains") else 0.0
    brenk = 1.0 if results.get("no_brenk") else 0.0
    nih = 1.0 if results.get("no_nih") else 0.0
    zinc = 1.0 if results.get("no_zinc") else 0.0
    safe_score = (pains * 0.4) + (brenk * 0.2) + (nih * 0.2) + (zinc * 0.2)
    
    # 5. Synthesis / Complexity (0-1)
    # SA score 1-10 (lower is better), Bertz complexity
    sa = results.get("sa_score", 10.0)
    sa_comp = 1.0 - (min(10.0, sa) - 1.0) / 9.0
    
    complexity = results.get("BertzCT", 1000)
    c_comp = 1.0 - min(1.0, complexity / 1500)
    
    syn_score = (sa_comp * 0.7) + (c_comp * 0.3)
    
    components = {
        "Structure": round(s_score, 2),
        "Compliance": round(prop_score, 2),
        "Drug-Likeness": round(p_score, 2),
        "Safety": round(safe_score, 2),
        "Synthesis": round(syn_score, 2)
    }
    
    weighted_total = (
        s_score * weights["structure"] +
        prop_score * weights["physchem"] +
        p_score * weights["drug_likeness"] +
        safe_score * weights["safety"] +
        syn_score * weights["complexity"]
    )
    
    final_score = round(weighted_total * 100, 2)
    grade = get_grade(final_score)
    
    return {
        "score": final_score,
        "grade": grade,
        "components": components,
        "weights": weights
    }

def get_grade(score):
    if score >= 90: return "A+"
    if score >= 80: return "A"
    if score >= 70: return "B+"
    if score >= 60: return "B"
    if score >= 50: return "C"
    return "F"
