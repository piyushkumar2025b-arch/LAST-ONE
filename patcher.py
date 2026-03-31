import os
import re

def patch_app():
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Bug 1: Missing private fields in synthetic loop
    # Location: before data.append(new_c) around line 2853
    # Wait, in the source it's `data.append(new_c)` inside the synthetic loop.
    private_fields = """                        new_c.setdefault("_hia", bool(new_c.get("tPSA", 100) < 142))
                        new_c.setdefault("_bbb", bool(new_c.get("tPSA", 100) < 79 and -2 < new_c.get("LogP", 3) < 6))
                        new_c.setdefault("_pains", False)
                        new_c.setdefault("_herg", "LOW")
                        new_c.setdefault("_qed", new_c.get("QED", 0.5))
                        new_c.setdefault("_sa", new_c.get("SA_Score", 5.0))
                        new_c.setdefault("_fp", None)
                        new_c.setdefault("_vc", 0)
                        new_c.setdefault("_org", True)
                        new_c.setdefault("_lp", new_c.get("LogP", 2.5))
                        new_c.setdefault("_mw", new_c.get("MW", 350.0))
                        new_c.setdefault("_tp", new_c.get("tPSA", 80.0))
                        new_c.setdefault("_rot", new_c.get("RotBonds", 5))
                        new_c.setdefault("_sim", 0.1)
                        new_c.setdefault("_hbd", 2)
                        new_c.setdefault("_hba", 5)
                        new_c.setdefault("_ar", 2)
                        new_c.setdefault("_cm", 5.0)
                        new_c.setdefault("_ames", "Low Risk")
                        new_c.setdefault("_af", [])
                        new_c.setdefault("_hf", [])
                        new_c.setdefault("_ls", -3.0)
                        new_c.setdefault("_sl", "Moderate")
                        new_c.setdefault("_sc", "warn")
                        new_c.setdefault("_cx", 40.0)
                        new_c.setdefault("_fsp3", 0.3)
                        new_c.setdefault("_vl", [])
                        new_c.setdefault("_h", int(new_c.get("MW", 350) / 14))
                        new_c.setdefault("_rings", 2)
                        new_c.setdefault("_stereo", 0)
                        new_c.setdefault("_elems", {"C": 20, "H": 24, "N": 2, "O": 3})
                        new_c.setdefault("_meta", {})
                        new_c.setdefault("_conf", "")
                        new_c.setdefault("_ld", new_c.get("LogP", 2.5))
                        new_c.setdefault("_ppb", "50-85%")
                        new_c.setdefault("_rc", "Moderate")
                        new_c.setdefault("_gc", {})
                        new_c.setdefault("_frags", {})
                        new_c.setdefault("_war", [])
                        new_c.setdefault("_iso", [])
                        new_c.setdefault("_diss", "Moderate")
                        new_c.setdefault("_eco", "Unknown")
                        new_c.setdefault("_cost", "Moderate")
                        new_c.setdefault("_dfi", "Low")
                        new_c.setdefault("_barcode", f"CPD-SYN-{i:04d}")
                        new_c.setdefault("_v15", {})
                        new_c.setdefault("_v20", {})
                        new_c.setdefault("_acc", {})
                        new_c.setdefault("_v50", {})
                        new_c.setdefault("_sa_lbl", "Moderate")
                        new_c.setdefault("_cyp", {})
                        new_c.setdefault("PromiscuityRisk", random.choice(["Low", "Low", "Medium", "High"]))
                        data.append(new_c)"""
    content = content.replace("data.append(new_c)", private_fields, 1)

    # Bug 2: _fp None crashes similarity matrix
    content = content.replace(
        'n=len(display_data); fps=[d["_fp"] for d in display_data]',
        'n=len(display_data); fps=[d["_fp"] if (d.get("_fp") is not None) else None for d in display_data]'
    )
    content = content.replace(
        'mat=np.array([[DataStructs.TanimotoSimilarity(fps[i],fps[j]) for j in range(n)] for i in range(n)])',
        'mat=np.array([[DataStructs.TanimotoSimilarity(fps[i],fps[j]) if fps[i] is not None and fps[j] is not None else 0.0 for j in range(n)] for i in range(n)])'
    )
    # PCA is already correct for fps array but uses float conversion
    
    # Bug 3: move jitter function
    jitter_def = """                    # Jitter helper — defined once outside loop
                    def jitter(val, noise=0.15, min_val=0):
                        try:
                            v = float(val)
                            return max(min_val, round(v * random.uniform(1-noise, 1+noise), 2))
                        except Exception:
                            return val

"""
    content = content.replace(jitter_def, "")
    # insert at top-ish, e.g. after imports or before analyze cached
    content = content.replace("def _analyze_cached(smiles_tuple: tuple) -> list:", 
'''def jitter(val, noise=0.15, min_val=0):
    try:
        v = float(val)
        return max(min_val, round(v * random.uniform(1-noise, 1+noise), 2))
    except Exception:
        return val

def _analyze_cached(smiles_tuple: tuple) -> list:''')

    # Bug 4: dict access replaced by .get in jitter block
    content = content.replace('new_c["MW"] = jitter(new_c["MW"]', 'new_c["MW"] = jitter(new_c.get("MW", 350)')
    content = content.replace('new_c["LogP"] = round(float(new_c["LogP"])', 'new_c["LogP"] = round(float(new_c.get("LogP", 2.5))')
    content = content.replace('new_c["tPSA"] = jitter(new_c["tPSA"]', 'new_c["tPSA"] = jitter(new_c.get("tPSA", 80.0)')
    content = content.replace('new_c["QED"] = max(0.01, min(0.99, jitter(new_c["QED"]', 'new_c["QED"] = max(0.01, min(0.99, jitter(new_c.get("QED", 0.5)')
    content = content.replace('new_c["LeadScore"] = int(max(30, min(95, jitter(new_c["LeadScore"]', 'new_c["LeadScore"] = int(max(30, min(95, jitter(new_c.get("LeadScore", 50)')
    content = content.replace('new_c["OralBioScore"] = int(max(20, min(95, jitter(new_c["OralBioScore"]', 'new_c["OralBioScore"] = int(max(20, min(95, jitter(new_c.get("OralBioScore", 60)')
    content = content.replace('new_c["SA_Score"] = max(1.0, min(10.0, jitter(new_c["SA_Score"]', 'new_c["SA_Score"] = max(1.0, min(10.0, jitter(new_c.get("SA_Score", 5.0)')
    content = content.replace('new_c["NP_Score"] = max(0, min(100, jitter(new_c["NP_Score"]', 'new_c["NP_Score"] = max(0, min(100, jitter(new_c.get("NP_Score", 50)')
    content = content.replace('new_c["Stress"] = max(0, min(100, jitter(new_c["Stress"]', 'new_c["Stress"] = max(0, min(100, jitter(new_c.get("Stress", 50)')
    content = content.replace('if new_c["MW"] > 500:', 'if new_c.get("MW", 0) > 500:')
    content = content.replace('if new_c["LogP"] > 5:', 'if new_c.get("LogP", 0) > 5:')
    content = content.replace('ext["Heavy_Atom_Count"] = int(new_c["MW"] / 14)', 'ext["Heavy_Atom_Count"] = int(new_c.get("MW", 350) / 14)')
    content = content.replace('ext["BBB_Penetration"] = "Yes" if new_c["tPSA"] < 79 and new_c["LogP"] > 0 and new_c["LogP"] < 5.5 else "No"',
                              'ext["BBB_Penetration"] = "Yes" if new_c.get("tPSA", 100) < 79 and new_c.get("LogP", 0) > 0 and new_c.get("LogP", 0) < 5.5 else "No"')
    content = content.replace('ext["Ligand_Efficiency"] = max(0.1, round(new_c["QED"] / (new_c["MW"] / 100), 2))',
                              'ext["Ligand_Efficiency"] = max(0.1, round(new_c.get("QED", 0.5) / (new_c.get("MW", 350) / 100), 2))')
    
    content = content.replace('if new_c["LeadScore"] >= 80:', 'if new_c.get("LeadScore", 0) >= 80:')
    content = content.replace('elif new_c["LeadScore"] >= 60:', 'elif new_c.get("LeadScore", 0) >= 60:')
    content = content.replace('elif new_c["LeadScore"] >= 40:', 'elif new_c.get("LeadScore", 0) >= 40:')
    content = content.replace('s_score = jitter(new_c["LeadScore"], 0.05)', 's_score = jitter(new_c.get("LeadScore", 50), 0.05)')
    content = content.replace('round(new_c["QED"], 2)', 'round(new_c.get("QED", 0.5), 2)')
    content = content.replace('round(1.0 - (new_c["SA_Score"] / 10), 2)', 'round(1.0 - (new_c.get("SA_Score", 5.0) / 10), 2)')


    # Bug 8: data_engine.py fallback stats
    content = content.replace('''@staticmethod
    def get_dataset_stats():
        return {}''', '''@staticmethod
    def get_dataset_stats():
        return {"compound_count": 0, "feature_count": 0, "status": "unavailable"}''')
    
    # Bug 10: @st.cache_resource -> @st.cache_data
    content = content.replace('@st.cache_resource(show_spinner=False)\ndef _analyze_cached(', '@st.cache_data(show_spinner=False)\ndef _analyze_cached(')

    # Bug 11: .get() access in stat strip
    content = content.replace('hia_ok = sum(1 for d in display_data if d["_hia"])', 'hia_ok = sum(1 for d in display_data if d.get("_hia", False))')
    content = content.replace('bbb_ok = sum(1 for d in display_data if d["_bbb"])', 'bbb_ok = sum(1 for d in display_data if d.get("_bbb", False))')
    content = content.replace('pf     = sum(1 for d in display_data if d["_pains"])', 'pf     = sum(1 for d in display_data if d.get("_pains", False))')
    content = content.replace('hh     = sum(1 for d in display_data if d["_herg"]=="HIGH")', 'hh     = sum(1 for d in display_data if d.get("_herg", "LOW") == "HIGH")')
    content = content.replace('aqed   = sum(d["_qed"] for d in data)/total', 'aqed   = sum(d.get("_qed", d.get("QED", 0.5)) for d in data)/total')
    content = content.replace('als    = sum(d["LeadScore"] for d in data)/total', 'als    = sum(d.get("LeadScore", 0) for d in data)/total')
    content = content.replace('asa    = sum(d["_sa"] for d in data)/total', 'asa    = sum(d.get("_sa", d.get("SA_Score", 5.0)) for d in data)/total')

    # Bug 13: PromiscuityRisk missing in analyze()
    promiscuity_snippet = """        r["PromiscuityRisk"]="Low" if sum(1 for v in cyp.values() if v["hit"]) <= 1 else "Medium" if sum(1 for v in cyp.values() if v["hit"]) <= 3 else "High"
        r["_tips"]=opt_tips(r)"""
    # replacing the current `r["PromiscuityRisk"]=promiscuity(r)` or adding if it doesn't match
    if 'r["PromiscuityRisk"]=promiscuity(r)' in content:
        content = content.replace('r["PromiscuityRisk"]=promiscuity(r)', 'r["PromiscuityRisk"]="Low" if sum(1 for v in cyp.values() if v["hit"]) <= 1 else "Medium" if sum(1 for v in cyp.values() if v["hit"]) <= 3 else "High"')
    else:
        # just append before results.append(r)
        content = content.replace('results.append(r)', 'r["PromiscuityRisk"]="Low" if sum(1 for v in cyp.values() if v.get("hit")) <= 1 else "Medium" if sum(1 for v in cyp.values() if v.get("hit")) <= 3 else "High"\n        results.append(r)')

    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)

def patch_chemo_scoring():
    path = "chemo_scoring.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding='utf-8') as f:
        c = f.read()
    if "def get_chemoscore_pkg(" not in c:
        c += '''\ndef get_chemoscore_pkg(results):
    """Wrapper that calls calculate_chemo_score and returns full package dict."""
    pkg = calculate_chemo_score(results)
    return {
        "score": pkg.get("score", 0.0),
        "grade": pkg.get("grade", "F"),
        "components": pkg.get("components", {}),
        "weights": pkg.get("weights", {}),
    }\n'''
        with open(path, "w", encoding='utf-8') as f:
            f.write(c)

def patch_smiles():
    path = "smiles_input_panel.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding='utf-8') as f:
        c = f.read()
    c = c.replace('"Lisinopril": "OC(=O)[C@@H](CCCl)N",', '"Lisinopril": "NCCCC[C@@H](N[C@@H](CCc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O)C(=O)O",')
    with open(path, "w", encoding='utf-8') as f:
        f.write(c)

def patch_full_report():
    path = "pages/full_report.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding='utf-8') as f:
        c = f.read()
    c = c.replace('_data = st.session_state[_synth_keys[0]]\\nif not _data:', 
                  '_data = st.session_state.get(_synth_keys[0]) if _synth_keys else None\\nif not _data or not isinstance(_data, list):')
    c = c.replace('''if _synth_keys:
    _data = st.session_state[_synth_keys[0]]
if not _data:''', '''if _synth_keys:
    _data = st.session_state.get(_synth_keys[0]) if _synth_keys else None
if not _data or not isinstance(_data, list):''')
    with open(path, "w", encoding='utf-8') as f:
        f.write(c)

def patch_visualization():
    path = "visualization_app/app.py"
    if not os.path.exists(path): return
    with open(path, "r", encoding='utf-8') as f:
        c = f.read()
    if "# NOTE: This is the standalone visualization micro-app." not in c:
        c = "# NOTE: This is the standalone visualization micro-app.\\n# The Streamlit multi-page version lives at pages/visualization.py\\n# Keep these in sync or consolidate into one file.\\n" + c
        with open(path, "w", encoding='utf-8') as f:
            f.write(c)

def fix_bare_excepts():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                p = os.path.join(root, file)
                with open(p, "r", encoding='utf-8') as f:
                    c = f.read()
                # Use regex to find `except Exception:` or `except Exception:`
                # Only replace `except Exception:` with `except Exception:`
                # We need to make sure we don't replace `except Exception:` with `except Exception Exception:`
                new_c = re.sub(r'except\s*:', 'except Exception:', c)
                if new_c != c:
                    with open(p, "w", encoding='utf-8') as f:
                        f.write(new_c)

if __name__ == "__main__":
    patch_app()
    patch_chemo_scoring()
    patch_smiles()
    patch_full_report()
    patch_visualization()
    fix_bare_excepts()
    print("Done")
