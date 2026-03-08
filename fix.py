content = open('app.py', encoding='utf-8').read()

content = content.replace(
    'from rdkit.Chem import (Descriptors, Draw, AllChem, DataStructs, QED,\n                        rdMolDescriptors, Crippen)',
    'from rdkit.Chem import (Descriptors, AllChem, DataStructs, QED,\n                        rdMolDescriptors, Crippen)\ntry:\n    from rdkit.Chem import Draw as _Draw\n    _DRAW_OK = True\nexcept Exception:\n    _Draw = None\n    _DRAW_OK = False'
)

content = content.replace(
    'data:image/png;base64,{mol_img_b64(',
    '{mol_img_src('
)

open('app.py', 'w', encoding='utf-8').write(content)
print('DONE')