content = open('app.py', encoding='utf-8').read()

old = '    st.dataframe(df_show.style\n        .background_gradient(cmap="YlOrRd", subset=["LeadScore","OralBioScore"])\n        .background_gradient(cmap="Reds",   subset=["PromiscuityRisk","SA_Score","CYP_Hits"])\n        .background_gradient(cmap="Blues",  subset=["Sim"])\n        .background_gradient(cmap="Greens", subset=["QED"]),\n        use_container_width=True, height=min(80+34*total,320))'

new = '    st.dataframe(df_show, use_container_width=True, height=min(80+34*total,320))'

if old in content:
    content = content.replace(old, new)
    print('FIXED')
else:
    print('NOT FOUND')

open('app.py', 'w', encoding='utf-8').write(content)