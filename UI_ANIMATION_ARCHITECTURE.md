# ⬡ ChemoFilter: UI Animation & "Crystalline Obsidian" Architecture

**The Engineering of a Premium Scientific Interface**  
*CSS Transitions, WebGL 3D Visualization, and Glassmorphism*

---

## 1. Executive Overview

ChemoFilter was designed with the philosophy that **Scientific Software should not be Boring.** The "Crystalline Obsidian" design system is built to "WOW" evaluators and judges at the MDP 2026 showcase while maintaining high information density.

---

## 2. Core CSS Design Tokens (Obsidian Theme)

All UI elements are styled using a custom CSS injector in `app.py`:

*   **Background:** Deep Obsidian (#0B0E14) with a subtle radial gradient.
*   **Accents:** Neon-Cyan (#00F5FF) and Toxic-Orange (#FF4500) for "Hazard" flags.
*   **Glassmorphism:** `backdrop-filter: blur(10px)` applied to all metric cards and sidebars.

---

## 3. The "Skeleton Loader" Animation

Because Cheminformatics calculations can be slow ($\approx 1s$/compound), we use **Skeleton Loaders** to provide instant visual feedback.

1.  **Logic:** An empty, glowing outline is rendered first.
2.  **CSS:** `animation: glow 1.5s infinite alternate;`.
3.  **Result:** The user perceives the app as "fast" even while the 9-Tier RDKit engine is computing at the CPU level.

---

## 4. WebGL 3D Molecule Transitions

The **"3D Conformer Explorer"** tab uses **WebGL** to render molecular coordinates:

*   **Logic:** 2D SMILES $\rightarrow$ RDKit 3D minimization $\rightarrow$ JSON Object $\rightarrow$ WebGL Canvas.
*   **Aesthetics:** Smooth rotation, atomic-glow effects, and "Phantom Atoms" (showing potential internal H-bonds) provided by the `py3dmol` library.

---

## 5. Information Density & Tooltips

To prevent "Tab-Bloat," we use **Floating Tooltips** and **Contextual Hover States**:

1.  **Implementation:** Hovering over a metric like **LogP** triggers a `terminology.py` lookup.
2.  **Display:** A glass-morphic popup appears explaining the scientific significance and the Lipinski threshold ($<5$).

---

## 6. Performance vs. Aesthetics

*   **No Image Placeholders:** All icons (⬡, 🧪, 🤖) are rendered as vectorized SVG or High-DPI emojis to keep the `app.py` payload under 500KB.
*   **Selective Rendering:** Tabs that are not active are "lazy-loaded," preventing the UI from locking up during massive dataset screenings.

---

## 7. How to Modify the Design System

To update the global aesthetic:
1.  Navigate to `ui_upgrade.py`.
2.  Modify the `:root` variables for `--primary-cyan` or `--bg-obsidian`.
3.  Restart the Streamlit server to see the changes applied across all **40+ Analytical Tabs**.
