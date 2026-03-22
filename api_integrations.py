"""
api_integrations.py
────────────────────────────────────────────────────────────────────────────
ChemoFilter · External API Integration Module
• PubChem REST API  — compound enrichment, synonyms, canonical SMILES
• ChEMBL REST API   — bioactivity data, target interactions
• PDB REST API      — protein structure context
• All calls: lazy, @st.cache_data(ttl=86400), timeout=5s, full fallback
• App works 100% without internet — APIs are optional enrichment only
────────────────────────────────────────────────────────────────────────────
"""

import streamlit as st
import urllib.parse
import json

# ── Safe imports ──────────────────────────────────────────────────────────
try:
    import requests as _req
    _REQ_OK = True
except Exception:
    _req = None
    _REQ_OK = False

_TIMEOUT = 5  # seconds — all API calls capped here

# ─────────────────────────────────────────────────────────────────────────────
# FALLBACK STRUCTURES — returned when any API fails
# ─────────────────────────────────────────────────────────────────────────────

_PUBCHEM_FALLBACK = {
    "source":       "local_fallback",
    "name":         "N/A",
    "iupac_name":   "N/A",
    "formula":      "N/A",
    "cid":          None,
    "synonyms":     [],
    "canonical_smiles": None,
    "inchikey":     "N/A",
    "xlogp":        None,
    "tpsa":         None,
    "hbd":          None,
    "hba":          None,
    "mw":           None,
    "rotatable_bonds": None,
    "complexity":   None,
    "charge":       None,
    "error":        None,
}

_CHEMBL_FALLBACK = {
    "source":       "local_fallback",
    "chembl_id":    None,
    "bioactivities": [],
    "targets":      [],
    "assay_count":  0,
    "error":        None,
}

_PDB_FALLBACK = {
    "source":       "local_fallback",
    "entries":      [],
    "count":        0,
    "error":        None,
}


# ─────────────────────────────────────────────────────────────────────────────
# 1. PUBCHEM API
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=86400, show_spinner=False)
def fetch_pubchem_by_smiles(smiles: str) -> dict:
    """
    Fetch PubChem compound data by canonical SMILES.
    Returns full property dict. Cached 24h. Falls back gracefully.
    """
    if not _REQ_OK or not smiles or not smiles.strip():
        return {**_PUBCHEM_FALLBACK, "error": "No SMILES provided or requests unavailable"}
    try:
        enc = urllib.parse.quote(smiles.strip())
        base = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

        # Step 1: get CID
        url_cid = f"{base}/compound/smiles/{enc}/cids/JSON"
        r = _req.get(url_cid, timeout=_TIMEOUT)
        r.raise_for_status()
        cid_data = r.json()
        cids = cid_data.get("IdentifierList", {}).get("CID", [])
        if not cids:
            return {**_PUBCHEM_FALLBACK, "error": "Compound not found in PubChem"}
        cid = cids[0]

        # Step 2: get properties
        props = "MolecularFormula,MolecularWeight,CanonicalSMILES,InChIKey," \
                "IUPACName,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount," \
                "RotatableBondCount,Complexity,Charge"
        url_props = f"{base}/compound/cid/{cid}/property/{props}/JSON"
        r2 = _req.get(url_props, timeout=_TIMEOUT)
        r2.raise_for_status()
        pdata = r2.json().get("PropertyTable", {}).get("Properties", [{}])[0]

        # Step 3: get synonyms (first 5)
        url_syn = f"{base}/compound/cid/{cid}/synonyms/JSON"
        try:
            r3 = _req.get(url_syn, timeout=_TIMEOUT)
            r3.raise_for_status()
            syns = r3.json().get("InformationList", {}).get("Information", [{}])[0].get("Synonym", [])[:5]
        except Exception:
            syns = []

        return {
            "source":          "pubchem",
            "cid":             cid,
            "name":            syns[0] if syns else pdata.get("IUPACName", "N/A"),
            "iupac_name":      pdata.get("IUPACName", "N/A"),
            "formula":         pdata.get("MolecularFormula", "N/A"),
            "synonyms":        syns,
            "canonical_smiles": pdata.get("CanonicalSMILES"),
            "inchikey":        pdata.get("InChIKey", "N/A"),
            "xlogp":           pdata.get("XLogP"),
            "tpsa":            pdata.get("TPSA"),
            "hbd":             pdata.get("HBondDonorCount"),
            "hba":             pdata.get("HBondAcceptorCount"),
            "mw":              pdata.get("MolecularWeight"),
            "rotatable_bonds": pdata.get("RotatableBondCount"),
            "complexity":      pdata.get("Complexity"),
            "charge":          pdata.get("Charge"),
            "error":           None,
        }

    except Exception as e:
        return {**_PUBCHEM_FALLBACK, "error": str(e)[:120]}


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_pubchem_by_name(name: str) -> dict:
    """Fetch PubChem data by compound name. Returns canonical SMILES and properties."""
    if not _REQ_OK or not name or not name.strip():
        return {**_PUBCHEM_FALLBACK, "error": "No name provided"}
    try:
        enc = urllib.parse.quote(name.strip())
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{enc}/property/CanonicalSMILES,IUPACName,MolecularFormula,MolecularWeight/JSON"
        r = _req.get(url, timeout=_TIMEOUT)
        r.raise_for_status()
        props = r.json().get("PropertyTable", {}).get("Properties", [{}])[0]
        smiles = props.get("CanonicalSMILES", "")
        if smiles:
            return fetch_pubchem_by_smiles(smiles)
        return {**_PUBCHEM_FALLBACK, "error": "No SMILES in response"}
    except Exception as e:
        return {**_PUBCHEM_FALLBACK, "error": str(e)[:120]}


# ─────────────────────────────────────────────────────────────────────────────
# 2. ChEMBL API
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=86400, show_spinner=False)
def fetch_chembl_by_smiles(smiles: str) -> dict:
    """
    Search ChEMBL for compound by SMILES similarity.
    Returns bioactivity data for top hit. Cached 24h.
    """
    if not _REQ_OK or not smiles or not smiles.strip():
        return {**_CHEMBL_FALLBACK, "error": "No SMILES provided"}
    try:
        enc = urllib.parse.quote(smiles.strip())
        base = "https://www.ebi.ac.uk/chembl/api/data"

        # Similarity search (70% threshold)
        url = f"{base}/similarity/{enc}/70.json?limit=5"
        r = _req.get(url, timeout=_TIMEOUT)
        r.raise_for_status()
        mols = r.json().get("molecules", [])

        if not mols:
            return {**_CHEMBL_FALLBACK, "error": "No similar compounds in ChEMBL"}

        top_hit = mols[0]
        chembl_id = top_hit.get("molecule_chembl_id", "")

        # Get bioactivities for top hit
        url_bio = f"{base}/activity.json?molecule_chembl_id={chembl_id}&limit=10"
        r2 = _req.get(url_bio, timeout=_TIMEOUT)
        r2.raise_for_status()
        activities_raw = r2.json().get("activities", [])

        activities = []
        for a in activities_raw[:8]:
            if a.get("standard_value") and a.get("target_pref_name"):
                activities.append({
                    "target":     a.get("target_pref_name", "Unknown Target"),
                    "type":       a.get("standard_type", "Activity"),
                    "value":      a.get("standard_value"),
                    "units":      a.get("standard_units", ""),
                    "assay_desc": a.get("assay_description", ""),
                    "doc_year":   a.get("document_year"),
                })

        # Get target list
        url_tgt = f"{base}/target.json?molecule_chembl_id={chembl_id}&limit=5"
        try:
            r3 = _req.get(url_tgt, timeout=_TIMEOUT)
            r3.raise_for_status()
            targets = [t.get("pref_name", "") for t in r3.json().get("targets", [])[:5]
                       if t.get("pref_name")]
        except Exception:
            targets = []

        return {
            "source":       "chembl",
            "chembl_id":    chembl_id,
            "similarity":   top_hit.get("similarity", 0),
            "bioactivities": activities,
            "targets":      targets,
            "assay_count":  len(activities),
            "mol_name":     top_hit.get("pref_name") or chembl_id,
            "error":        None,
        }

    except Exception as e:
        return {**_CHEMBL_FALLBACK, "error": str(e)[:120]}


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_chembl_targets(query: str) -> list:
    """Search ChEMBL targets by keyword. Returns list of target dicts."""
    if not _REQ_OK or not query:
        return []
    try:
        enc = urllib.parse.quote(query.strip())
        url = f"https://www.ebi.ac.uk/chembl/api/data/target/search.json?q={enc}&limit=5"
        r = _req.get(url, timeout=_TIMEOUT)
        r.raise_for_status()
        targets = r.json().get("targets", [])
        return [
            {
                "name":       t.get("pref_name", "Unknown"),
                "type":       t.get("target_type", ""),
                "organism":   t.get("organism", ""),
                "chembl_id":  t.get("target_chembl_id", ""),
            }
            for t in targets[:5]
        ]
    except Exception:
        return []


# ─────────────────────────────────────────────────────────────────────────────
# 3. PROTEIN DATA BANK (PDB)
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=86400, show_spinner=False)
def fetch_pdb_entries(query: str) -> dict:
    """
    Search PDB for protein structures matching a query term.
    Returns entry metadata. Cached 24h.
    """
    if not _REQ_OK or not query:
        return {**_PDB_FALLBACK, "error": "No query provided"}
    try:
        url = "https://search.rcsb.org/rcsbsearch/v2/query"
        payload = {
            "query": {
                "type": "terminal",
                "service": "full_text",
                "parameters": {"value": query.strip()}
            },
            "return_type": "entry",
            "request_options": {"paginate": {"start": 0, "rows": 5}}
        }
        r = _req.post(url, json=payload, timeout=_TIMEOUT)
        r.raise_for_status()
        result = r.json()
        entries = result.get("result_set", [])

        if not entries:
            return {**_PDB_FALLBACK, "error": f"No PDB entries found for '{query}'"}

        entry_data = []
        for e in entries[:5]:
            pdb_id = e.get("identifier", "")
            entry_data.append({
                "pdb_id":   pdb_id,
                "score":    round(e.get("score", 0), 3),
                "url":      f"https://www.rcsb.org/structure/{pdb_id}",
            })

        return {
            "source":  "pdb",
            "entries": entry_data,
            "count":   result.get("total_count", len(entries)),
            "error":   None,
        }
    except Exception as e:
        return {**_PDB_FALLBACK, "error": str(e)[:120]}


# ─────────────────────────────────────────────────────────────────────────────
# 4. UNIFIED COMPOUND ENRICHMENT
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_data(ttl=86400, show_spinner=False)
def enrich_compound(smiles: str) -> dict:
    """
    Full enrichment pipeline: PubChem + ChEMBL in one call.
    Both are cached independently. Returns combined dict.
    """
    pubchem = fetch_pubchem_by_smiles(smiles)
    chembl  = fetch_chembl_by_smiles(smiles)
    return {
        "pubchem": pubchem,
        "chembl":  chembl,
        "smiles":  smiles,
        "enriched": pubchem.get("error") is None or chembl.get("error") is None,
    }


# ─────────────────────────────────────────────────────────────────────────────
# 5. UI RENDERER — "External Scientific Data" section
# ─────────────────────────────────────────────────────────────────────────────

def render_external_data_section(compound: dict):
    """
    Renders the External Scientific Data enrichment section.
    All API calls are lazy — only fire on button click.
    Fully safe if all APIs fail.
    """
    smiles = compound.get("SMILES") or compound.get("smi") or ""
    cpd_id = compound.get("ID", "Compound")

    st.markdown("---")
    st.markdown("### 🔬 External Scientific Data Enrichment")
    st.caption(
        "Fetches real-time data from PubChem, ChEMBL, and PDB. "
        "Optional enrichment only — core analysis is unaffected if APIs are unavailable."
    )

    if not smiles:
        st.info("No SMILES available for this compound — cannot query external databases.")
        return

    # ── PubChem Section ───────────────────────────────────────────────────
    with st.expander("🧪 PubChem — Compound Identity & Verified Properties", expanded=False):
        _pc_key = f"_ext_pubchem_{cpd_id}"
        if not st.session_state.get(_pc_key):
            st.markdown(
                '<span style="font-size:.78rem;color:#94a3b8">'
                'Retrieves verified molecular properties, IUPAC name, synonyms, '
                'and structure from the NIH PubChem database.</span>',
                unsafe_allow_html=True)
            if st.button("🔍 Fetch PubChem Data", key=f"_btn_pc_{cpd_id}"):
                st.session_state[_pc_key] = True
                st.rerun()
        else:
            with st.spinner("Querying PubChem..."):
                pc = fetch_pubchem_by_smiles(smiles)

            if pc.get("error"):
                st.warning(f"PubChem: {pc['error']}")
            else:
                c1, c2, c3 = st.columns(3)
                c1.metric("CID", pc.get("cid", "N/A"),
                          help="PubChem Compound Identifier (CID)")
                c2.metric("Molecular Formula", pc.get("formula", "N/A"))
                c3.metric("Molecular Weight (Da)", pc.get("mw", "N/A"),
                          help="Verified molecular weight from PubChem")

                st.markdown(f"**IUPAC Name:** `{pc.get('iupac_name', 'N/A')}`")
                st.markdown(f"**InChIKey:** `{pc.get('inchikey', 'N/A')}`")

                if pc.get("synonyms"):
                    st.markdown("**Known Names / Synonyms:** " +
                                " · ".join(f"`{s}`" for s in pc["synonyms"]))

                # Property comparison: PubChem vs local
                loc_mw   = compound.get("MW", "?")
                loc_logp = compound.get("LogP", "?")
                st.markdown("**Property Verification (PubChem vs Local Calculation):**")
                vcols = st.columns(4)
                vcols[0].metric("MW (PubChem)", pc.get("mw","?"),
                                delta=f"{round(float(pc['mw'])-float(loc_mw),2) if pc.get('mw') and loc_mw != '?' else '–'} Da",
                                help="Difference vs local RDKit calculation")
                vcols[1].metric("LogP (PubChem XLogP)", pc.get("xlogp","?"),
                                delta=f"{round(float(pc['xlogp'])-float(loc_logp),2) if pc.get('xlogp') and loc_logp != '?' else '–'}",
                                help="PubChem XLogP vs local Crippen LogP")
                vcols[2].metric("TPSA (Ų)", pc.get("tpsa","?"),
                                help="Topological Polar Surface Area from PubChem")
                vcols[3].metric("Rotatable Bonds", pc.get("rotatable_bonds","?"))

                st.markdown(
                    f'<a href="https://pubchem.ncbi.nlm.nih.gov/compound/{pc["cid"]}" '
                    f'target="_blank" style="color:#f5a623;font-size:.75rem">'
                    f'🔗 View on PubChem →</a>',
                    unsafe_allow_html=True)

    # ── ChEMBL Section ────────────────────────────────────────────────────
    with st.expander("🎯 ChEMBL — Bioactivity & Target Interaction Data", expanded=False):
        _ch_key = f"_ext_chembl_{cpd_id}"
        if not st.session_state.get(_ch_key):
            st.markdown(
                '<span style="font-size:.78rem;color:#94a3b8">'
                'Retrieves experimentally measured bioactivity data, IC₅₀ / Ki values, '
                'and known protein targets from the ChEMBL bioactivity database (EMBL-EBI).</span>',
                unsafe_allow_html=True)
            if st.button("🎯 Fetch ChEMBL Bioactivity Data", key=f"_btn_ch_{cpd_id}"):
                st.session_state[_ch_key] = True
                st.rerun()
        else:
            with st.spinner("Querying ChEMBL..."):
                ch = fetch_chembl_by_smiles(smiles)

            if ch.get("error"):
                st.warning(f"ChEMBL: {ch['error']}")
            else:
                st.markdown(
                    f"**Top Similar Compound:** `{ch.get('mol_name','N/A')}` "
                    f"(ChEMBL ID: `{ch.get('chembl_id','N/A')}`, "
                    f"Similarity: `{ch.get('similarity','?'):.0f}%`)"
                )

                if ch.get("targets"):
                    st.markdown("**Known Protein Targets:**")
                    for t in ch["targets"]:
                        st.markdown(
                            f'<span style="background:rgba(232,160,32,.08);'
                            f'border:1px solid rgba(232,160,32,.2);border-radius:4px;'
                            f'padding:2px 8px;font-size:.72rem;color:#f5a623;margin:2px;'
                            f'display:inline-block">{t}</span>',
                            unsafe_allow_html=True)

                if ch.get("bioactivities"):
                    st.markdown(f"**Experimental Bioactivity Data ({ch['assay_count']} assays):**")
                    import pandas as pd
                    df = pd.DataFrame(ch["bioactivities"])
                    df.columns = ["Target", "Activity Type", "Value", "Units",
                                  "Assay Description", "Publication Year"]
                    st.dataframe(df[["Target", "Activity Type", "Value", "Units",
                                     "Publication Year"]].head(8),
                                 use_container_width=True)
                else:
                    st.info("No experimental bioactivity data found for similar compounds.")

                st.markdown(
                    f'<a href="https://www.ebi.ac.uk/chembl/compound_report_card/{ch["chembl_id"]}/" '
                    f'target="_blank" style="color:#f5a623;font-size:.75rem">'
                    f'🔗 View on ChEMBL →</a>',
                    unsafe_allow_html=True)

    # ── PDB Section ───────────────────────────────────────────────────────
    with st.expander("🏗️ Protein Data Bank (PDB) — Target Structure Context", expanded=False):
        _pdb_key = f"_ext_pdb_{cpd_id}"
        pdb_query_key = f"_pdb_query_{cpd_id}"

        st.markdown(
            '<span style="font-size:.78rem;color:#94a3b8">'
            'Search the RCSB Protein Data Bank for protein structures related to '
            'your compound\'s likely target or mechanism.</span>',
            unsafe_allow_html=True)

        pdb_query = st.text_input(
            "Search PDB by target name or keyword",
            placeholder="e.g. kinase, EGFR, protease, GPCR",
            key=f"_pdb_q_{cpd_id}",
        )

        if st.button("🏗️ Search Protein Data Bank", key=f"_btn_pdb_{cpd_id}"):
            st.session_state[_pdb_key] = pdb_query or "drug target"
            st.rerun()

        if st.session_state.get(_pdb_key):
            query_used = st.session_state[_pdb_key]
            with st.spinner(f"Searching PDB for '{query_used}'..."):
                pdb = fetch_pdb_entries(query_used)

            if pdb.get("error"):
                st.warning(f"PDB: {pdb['error']}")
            else:
                st.markdown(f"**{pdb['count']} structures found.** Top results:")
                for entry in pdb["entries"]:
                    st.markdown(
                        f'<div style="display:flex;align-items:center;gap:12px;'
                        f'padding:6px 0;border-bottom:1px solid rgba(255,255,255,.05)">'
                        f'<code style="color:#f5a623;font-size:.8rem">{entry["pdb_id"]}</code>'
                        f'<a href="{entry["url"]}" target="_blank" '
                        f'style="color:#38bdf8;font-size:.75rem">View Structure ↗</a>'
                        f'<span style="color:#64748b;font-size:.65rem">'
                        f'Relevance: {entry["score"]}</span></div>',
                        unsafe_allow_html=True)

    # ── AI Name Lookup ────────────────────────────────────────────────────
    with st.expander("🔤 Drug Name Lookup — Search by Common Name", expanded=False):
        st.markdown(
            '<span style="font-size:.78rem;color:#94a3b8">'
            'Look up a drug by common name (e.g. aspirin, ibuprofen) to retrieve '
            'its canonical SMILES from PubChem for analysis.</span>',
            unsafe_allow_html=True)
        _nl_key = f"_ext_namelookup_{cpd_id}"
        name_query = st.text_input(
            "Enter drug name",
            placeholder="e.g. aspirin, caffeine, metformin",
            key=f"_name_q_{cpd_id}",
        )
        if st.button("🔍 Look Up by Name", key=f"_btn_nl_{cpd_id}"):
            if name_query.strip():
                with st.spinner(f"Looking up '{name_query}' on PubChem..."):
                    nl = fetch_pubchem_by_name(name_query)
                if nl.get("error"):
                    st.warning(f"Name lookup: {nl['error']}")
                elif nl.get("canonical_smiles"):
                    st.success(f"Found: `{nl['canonical_smiles']}`")
                    st.markdown(f"**IUPAC Name:** `{nl.get('iupac_name','N/A')}`")
                    st.markdown(
                        "Copy the SMILES above and paste it into the input panel to analyse this compound."
                    )
                else:
                    st.info("No canonical SMILES found.")
