import re
content = open('app.py', encoding='utf-8').read()

# Replace ALL **PT occurrences
content = content.replace('**PT,', 
    'paper_bgcolor="#0c1220", plot_bgcolor="#0c1220", font=dict(family="IBM Plex Mono", color="rgba(200,222,255,0.45)", size=10),')

# Fix invalid title
content = content.replace('title="tPSA (A2)"', 'title="tPSA"')
content = content.replace('title="LogP (WLOGP)"', 'title="LogP"')

# Fix all titlefont deprecated key
content = re.sub(r'titlefont=dict\(([^)]+)\)', 
    lambda m: 'title=dict(font=dict(' + m.group(1) + '))', content)

open('app.py', 'w', encoding='utf-8').write(content)
print('DONE - remaining PT:', content.count('**PT'))