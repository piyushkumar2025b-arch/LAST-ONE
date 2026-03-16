
def calculate_chemo_score(results, weights=None):
    """
    results: dict from run_all_chemo_tests
    weights: dict with weights for different categories
    Returns a dictionary (Package) with:
      - score: float (0-100)
      - grade: str (A, B, C, F)
      - components: dict (breakdown of scores)
      - weights: dict (weights used)
    """
    if not results: return {"score": 0.0, "grade": "F", "components": {}, "weights": {}}
    
    if weights is None:
        weights = {
            "structure": 0.20,
            "physchem": 0.25,
            "drug_likeness": 0.25,
            "safety": 0.20,
            "synthesis": 0.10
        }
        
    # 1. Structure Score (0-1)
    s_score = 0.0
    s_factors = [
        results.get("valid", False),
        results.get("valence_ok", False),
        not results.get("disconnected", True),
        not results.get("highly_charged", True),
        results.get("normalized", False)
    ]
    s_score = sum(1.0 for f in s_factors if f) / len(s_factors)
    
    # 2. PhysChem Score (0-1)
    p_score = 0.0
    # QED is 0-1
    qed = results.get("qed", 0.0)
    # LogP target range 0-3 (central)
    lp = results.get("logp", 0.0)
    lp_score = 1.0 - min(1.0, abs(lp - 1.5) / 3.0)
    p_score = (qed * 0.6) + (lp_score * 0.4)
    
    # 3. Drug-Likeness Score (0-1)
    d_score = 0.0
    lipinski = 1.0 if results.get("lipinski") else 0.0
    fsp3 = results.get("fsp3", 0.0)
    # Target fsp3 > 0.4
    fsp3_score = min(1.0, fsp3 / 0.4)
    d_score = (lipinski * 0.7) + (fsp3_score * 0.3)
    
    # 4. Safety Score (0-1)
    safe_score = 0.0
    pains = 1.0 if results.get("no_pains") else 0.0
    brenk = 1.0 if results.get("no_brenk") else 0.0
    nih = 1.0 if results.get("no_nih") else 0.0
    reactive = 0.0 if results.get("reactive") else 1.0
    safe_score = (pains * 0.4) + (brenk * 0.2) + (nih * 0.2) + (reactive * 0.2)
    
    # 5. Synthesis Score (0-1)
    # SA score 1-10 (lower is better)
    sa = results.get("sa_score", 10.0)
    syn_score = 1.0 - (min(10.0, sa) - 1.0) / 9.0
    
    components = {
        "structure": round(s_score, 2),
        "physchem": round(p_score, 2),
        "drug_likeness": round(d_score, 2),
        "safety": round(safe_score, 2),
        "synthesis": round(syn_score, 2)
    }
    
    weighted_total = (
        s_score * weights["structure"] +
        p_score * weights["physchem"] +
        d_score * weights["drug_likeness"] +
        safe_score * weights["safety"] +
        syn_score * weights["synthesis"]
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
    if score >= 85: return "A+"
    if score >= 75: return "A"
    if score >= 65: return "B+"
    if score >= 55: return "B"
    if score >= 45: return "C"
    return "F"
