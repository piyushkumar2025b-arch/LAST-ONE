content = open('app.py', encoding='utf-8').read()

new_func = '''def mol_img_b64(mol, sz=(280,210)):
    try:
        from rdkit.Chem.Draw import rdMolDraw2D
        drawer = rdMolDraw2D.MolDraw2DSVG(sz[0], sz[1])
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        svg = drawer.GetDrawingText()
        return base64.b64encode(svg.encode()).decode() + "__SVG__"
    except Exception:
        pass
    return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="

def mol_img_src(mol, sz=(280,210)):
    raw = mol_img_b64(mol, sz)
    if raw.endswith("__SVG__"):
        return "data:image/svg+xml;base64," + raw[:-7]
    return "data:image/png;base64," + raw
'''

# Find and replace the old mol_img_b64
import re
content = re.sub(
    r'def mol_img_b64\(mol.*?return base64\.b64encode\(buf\.getvalue\(\)\)\.decode\(\)',
    new_func.strip(),
    content,
    flags=re.DOTALL
)

open('app.py', 'w', encoding='utf-8').write(content)
print('DONE')