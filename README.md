# ⬡ ChemoFilter — Crystalline Noir Edition v7
### VIT Chennai MDP 2026

A production-grade computational drug screening dashboard with a radically redesigned **Crystalline Noir** UI — amber gold on deep midnight navy, frosted glass panels, Playfair Display + IBM Plex Mono typography, animated gradient borders, and 21 active features.

---

## 🎨 UI Design Philosophy — Crystalline Noir
- **Palette**: Deep midnight navy `#080c14` · Amber gold `#f5a623` · Ice blue `#c8deff`
- **Typography**: Playfair Display (editorial display) + IBM Plex Mono (data/mono) + Cormorant Garamond (italic sub-heads)
- **Motifs**: Animated gold gradient borders · Frosted glass cards · Hex decorative elements · Twinkling star background · Grid texture overlay
- **Completely different from v6** — zero green terminal aesthetic

---

## 🚀 21 Features

### Core ADME
BOILED-EGG · Lipinski Ro5 · Veber/Ghose/Egan · QED · CNS MPO · ESOL · PAINS · hERG · Ames · Tanimoto

### New in v7 (UI-upgraded from v6)
SA Score · CYP Panel ×5 · Complexity Score · Elemental Donut · Promiscuity Risk · Lead Score™ · Oral Bio Score · AI Explainer · AI Analogues · Drug Repurposing Hint · Interactive Property Editor

### Visualisation
BOILED-EGG scatter · QED bar · SA bar · CYP heatmap · Radar chart · Similarity matrix · Parallel coordinates · PCA chemical space · vs Approved drugs · Element donut · Dual gauges

---

## 🛠️ Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Streamlit Cloud**: push to GitHub, connect at share.streamlit.io — `packages.txt` handles system deps automatically.

---

## 📦 Files
```
chemofilter_v7/
├── app.py              ← Main app (v7 Crystalline Noir)
├── requirements.txt    ← Python deps
├── packages.txt        ← System deps (Streamlit Cloud)
└── README.md
```

---

## 📚 References
| # | Reference | Year |
|---|---|---|
|[1]|Daina & Zoete, ChemMedChem 11:1117|2016|
|[2]|Lipinski et al., ADDR 46:3|2001|
|[3]|Delaney, JCICS 44:1000|2004|
|[4]|Bickerton et al., Nat Chem 4:90|2012|
|[5]|Wager et al., ACS Chem Neurosci 1:435|2010|
|[6]|Baell & Holloway, JMC 53:2719|2010|
|[7]|Ertl & Schuffenhauer, J Cheminf 1:8|2009|
|[8]|Rogers & Hahn, JCIM 50:742|2010|
|[9]|Landrum, RDKit|2006+|
