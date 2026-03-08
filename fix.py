content = open('app.py', encoding='utf-8').read()

old = '''update_layout(**PT,
        xaxis=dict(title="tPSA (A2)",range=[-10,220],gridcolor="rgba(245,166,35,0.06)",zeroline=False,
                   titlefont=dict(size=10,color="rgba(245,166,35,0.4)")),
        yaxis=dict(title="LogP (WLOGP)",range=[-4.5,9],gridcolor="rgba(245,166,35,0.06)",zeroline=False,
                   titlefont=dict(size=10,color="rgba(245,166,35,0.4)")),
        height=540,legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(size=10,family="IBM Plex Mono",color="rgba(200,222,255,0.5)")),
        margin=dict(l=60,r=40,t=20,b=60))'''

new = '''update_layout(**PT,
        xaxis=dict(title=dict(text="tPSA",font=dict(size=10,color="rgba(245,166,35,0.4)")),range=[-10,220],gridcolor="rgba(245,166,35,0.06)",zeroline=False),
        yaxis=dict(title=dict(text="LogP",font=dict(size=10,color="rgba(245,166,35,0.4)")),range=[-4.5,9],gridcolor="rgba(245,166,35,0.06)",zeroline=False),
        height=540,legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(size=10,family="IBM Plex Mono",color="rgba(200,222,255,0.5)")),
        margin=dict(l=60,r=40,t=20,b=60))'''

if old in content:
    content = content.replace(old, new)
    print('FIXED')
else:
    print('NOT FOUND')

open('app.py', 'w', encoding='utf-8').write(content)