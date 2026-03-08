content = open('app.py', encoding='utf-8').read()

old = 'update_layout(**PT,\n        xaxis=dict(title=dict(text="tPSA",font=dict(size=10,color="rgba(245,166,35,0.4)")),range=[-10,220],gridcolor="rgba(245,166,35,0.06)",zeroline=False),\n        yaxis=dict(title=dict(text="LogP",font=dict(size=10,color="rgba(245,166,35,0.4)")),range=[-4.5,9],gridcolor="rgba(245,166,35,0.06)",zeroline=False),\n        height=540,legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(size=10,family="IBM Plex Mono",color="rgba(200,222,255,0.5)")),\n        margin=dict(l=60,r=40,t=20,b=60))'

new = 'update_layout(\n        paper_bgcolor="#0c1220",plot_bgcolor="#0c1220",\n        font=dict(family="IBM Plex Mono",color="rgba(200,222,255,0.45)",size=10),\n        xaxis=dict(title="tPSA",range=[-10,220],gridcolor="rgba(245,166,35,0.06)",zeroline=False),\n        yaxis=dict(title="LogP",range=[-4.5,9],gridcolor="rgba(245,166,35,0.06)",zeroline=False),\n        height=540,legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(size=10,family="IBM Plex Mono",color="rgba(200,222,255,0.5)")),\n        margin=dict(l=60,r=40,t=20,b=60))'

if old in content:
    content = content.replace(old, new)
    print('FIXED')
else:
    print('NOT FOUND')

open('app.py', 'w', encoding='utf-8').write(content)