content = open('app.py', encoding='utf-8').read()

# Find and replace ALL update_layout(**PT in entire file
import re

def replace_pt(m):
    rest = m.group(1)
    return 'update_layout(\n        paper_bgcolor="#0c1220",plot_bgcolor="#0c1220",\n        font=dict(family="IBM Plex Mono",color="rgba(200,222,255,0.45)",size=10),' + rest

content = re.sub(r'update_layout\(\*\*PT,', 
    'update_layout(\n        paper_bgcolor="#0c1220",plot_bgcolor="#0c1220",\n        font=dict(family="IBM Plex Mono",color="rgba(200,222,255,0.45)",size=10),',
    content)

# Fix tPSA (A2) invalid title
content = content.replace('title="tPSA (A2)"', 'title="tPSA"')
content = content.replace("title='tPSA (A2)'", "title='tPSA'")

count = content.count('**PT')
print(f'Remaining **PT occurrences: {count}')
print('DONE')

open('app.py', 'w', encoding='utf-8').write(content)