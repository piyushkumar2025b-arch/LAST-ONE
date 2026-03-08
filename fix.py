content = open('app.py', encoding='utf-8').read()

old = '''PT = dict(
    paper_bgcolor="#0c1220",
    plot_bgcolor="#ffffff",
    font=dict(family="IBM Plex Mono, monospace", color="rgba(200,222,255,0.45)", size=10),
    xaxis=dict(gridcolor="rgba(245,166,35,0.06)", zeroline=False,
               tickfont=dict(size=9, family="IBM Plex Mono")),
    yaxis=dict(gridcolor="rgba(245,166,35,0.06)", zeroline=False,
               tickfont=dict(size=9, family="IBM Plex Mono")),
)'''

new = '''PT = dict(
    paper_bgcolor="#0c1220",
    plot_bgcolor="#ffffff",
    font=dict(family="IBM Plex Mono, monospace", color="rgba(200,222,255,0.45)", size=10),
)'''

if old in content:
    content = content.replace(old, new)
    print('FIXED')
else:
    print('NOT FOUND')

open('app.py', 'w', encoding='utf-8').write(content)