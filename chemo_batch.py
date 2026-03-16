
import pandas as pd
from rdkit import Chem
from chemo_filters import run_all_chemo_tests
from chemo_scoring import calculate_chemo_score

def process_molecule_batch(smiles_list, names=None, ref_smiles=None):
    if not names:
        names = [f"Mol_{i}" for i in range(len(smiles_list))]
    
    ref_mol = Chem.MolFromSmiles(ref_smiles) if ref_smiles else None
    
    batch_results = []
    for smi, name in zip(smiles_list, names):
        mol = Chem.MolFromSmiles(smi)
        if mol:
            res = run_all_chemo_tests(mol, ref_mol)
            res["name"] = name
            res["smiles"] = smi
            res["overall_score"] = calculate_chemo_score(res)
            batch_results.append(res)
        else:
            batch_results.append({
                "name": name,
                "smiles": smi,
                "valid": False,
                "overall_score": 0.0
            })
            
    return pd.DataFrame(batch_results)

def get_batch_statistics(data_list):
    """
    data_list: list of dicts (from app.py display_data)
    """
    if not data_list: return {}
    
    import pandas as pd
    df = pd.DataFrame(data_list)
    
    stats = {
        "count": len(df),
        "avg_chemoscore": df["ChemoScore"].mean() if "ChemoScore" in df else 0,
        "grade_dist": df["Grade"].value_counts().to_dict() if "Grade" in df else {},
    }
    
    # Property Ranges
    props = ["MW", "LogP", "tPSA", "QED", "SA_Score"]
    ranges = {}
    for p in props:
        if p in df:
            ranges[p.lower()] = {
                "min": round(df[p].min(), 2),
                "max": round(df[p].max(), 2),
                "avg": round(df[p].mean(), 2)
            }
    stats["property_ranges"] = ranges
    
    # Top Leads
    if "ChemoScore" in df:
        leads = df.sort_values("ChemoScore", ascending=False).head(10)
        stats["leads"] = leads[["ID", "SMILES", "Grade", "ChemoScore"]].to_dict(orient="records")
    else:
        stats["leads"] = []
        
    return stats
