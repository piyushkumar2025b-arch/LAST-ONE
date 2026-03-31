# ⬡ ChemoFilter: UI/UX Design System 

To elevate ChemoFilter from a basic Streamlit script into a clinical-grade, enterprise SaaS platform, we developed the **Crystalline Obsidian** design language.

This file documents the CSS injection protocols managed within `ui_upgrade.py`.

---

## 1. Design Philosophy
*   **Minimalist Density:** Scientific data is inherently heavy. Displaying 30 variables per molecule requires extreme padding discipline, sub-text fading, and distinct visual hierarchies.
*   **Non-Blocking Feedback:** Processing 500 molecules takes time. The UI must never "freeze." We utilize skeleton loaders and pulsing glow animations to imply background computation.
*   **Agnostic Theming:** The platform defaults to a strict dark mode (`#0c1220`) because organic chemists spend 10+ hours a day looking at molecular structures. High-contrast dark backgrounds reduce retinal fatigue.

## 2. Core Color Tokens
```css
:root {
  /* BACKGROUND SIGNATURES */
  --bg-void: #06090f;            /* Absolute background */
  --bg-surface: #0c1220;         /* Primary container backgrounds */
  --bg-elevated: #111827;        /* Hovered elements / modals */

  /* NEON SCIENTIFIC ACCENTS */
  --accent-cyan: #00f0ff;        /* Primary action indicators */
  --accent-gold: #f5a623;        /* Secondary highlights (Warnings) */
  --accent-green: #4ade80;       /* Perfect Pass / Grade A */
  --accent-red: #ff5c5c;         /* Toxicophore / hERG fail */
  
  /* TYPOGRAPHY OVERRIDES */
  --text-primary: #f0f4f8;       /* Headers, explicit data values */
  --text-muted: rgba(200, 222, 255, 0.45); /* Unit labels, tooltips */
}
```

## 3. Skeleton Loading Physics
Instead of using Streamlit's default blocking spinner, we override the DOM with CSS infinite keyframes.
```css
@keyframes pulse-data {
    0% { background-color: rgba(255,255,255,0.02); }
    50% { background-color: rgba(255,255,255,0.06); }
    100% { background-color: rgba(255,255,255,0.02); }
}
.skeleton-box {
    animation: pulse-data 1.5s infinite ease-in-out;
    border-radius: 4px;
}
```
This implies forward progress to the user while `fastparquet` asynchronously processes the dataset.

## 4. Typography Protocols
*   **Headers & Narrative Text:** `Inter` or `Syne`. Clean, geometric sans-serif for readability.
*   **Data Grids & Numerical Output:** `IBM Plex Mono` or `JetBrains Mono`. Monospaced fonts are strictly required for mathematical outputs (e.g., LogP = 4.234) so decimal points align vertically in tables.
*   **SMILES Strings:** `Courier New`. Explicitly styled to wrap safely without breaking character sequences.
