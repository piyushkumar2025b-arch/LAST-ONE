import re
content = open('app.py', encoding='utf-8').read()

# Fix 1: replace all titlefont= with the new format globally
content = re.sub(
    r'titlefont=dict\(([^)]+)\)',
    lambda m: 'title=dict(font=dict(' + m.group(1) + '))',
    content
)

# Fix 2: in fig_boiled_egg specifically, replace **PT with inlined values
old = '''update_layout(**PT,
        xaxis=dict(title="tPSA (A2)",range=[-10,220],gridcolor="rgba(245,166,35,0.06)",zeroline=False,
                   titlefont=dict(size=10,color="rgba(245,166,35,0.4)")),
        yaxis=dict(title="LogP (WLOGP)",range=[-4.5,9],gridcolor="rgba(245,166,35,0.06)",zeroline=False,
                   titlefont=dict(size=10,color="rgba(245,166,35,0.4)")),
        height=540,legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(size=10,family="IBM Plex Mono",color="rgba(200,222,255,0.5)")),
        margin=dict(l=60,r=40,t=20,b=60))'''

new = '''update_layout(
        paper_bgcolor="#0c1220",plot_bgcolor="#0c1220",
        font=dict(family="IBM Plex Mono, monospace",color="rgba(200,222,255,0.45)",size=10),
        xaxis=dict(title="tPSA",range=[-10,220],gridcolor="rgba(245,166,35,0.06)",zeroline=False),
        yaxis=dict(title="LogP",range=[-4.5,9],gridcolor="rgba(245,166,35,0.06)",zeroline=False),
        height=540,legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(size=10,family="IBM Plex Mono",color="rgba(200,222,255,0.5)")),
        margin=dict(l=60,r=40,t=20,b=60))'''

if old in content:
    content = content.replace(old, new)
    print('boiled_egg FIXED')
else:
    print('boiled_egg NOT FOUND - trying after titlefont fix')
    # try again after titlefont was already replaced above
    old2 = old.replace(
        'titlefont=dict(size=10,color="rgba(245,166,35,0.4)")',
        'title=dict(font=dict(size=10,color="rgba(245,166,35,0.4)"))'
    )
    if old2 in content:
        content = content.replace(old2, new)
        print('boiled_egg FIXED after titlefont sub')
    else:
        print('STILL NOT FOUND')

open('app.py', 'w', encoding='utf-8').write(content)