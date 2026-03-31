# ⬡ ChemoFilter: Brand Resources & Design Identity ⬡

**The Guidelines for the "Crystalline Obsidian" Design System**  
*Fonts, Colors, Logos, and Presentation Templates for VIT MDP 2026*

---

## 1. Executive Overview

The **ChemoFilter** brand was created to embody "Precision, Science, and Modernity." The "Crystalline Obsidian" design system is not just aesthetic; it’s a UI framework that makes complex ADMET data intuitive and visually striking.

---

## 2. Core Color Palette (Hex/HSL)

| Color Name | Hex Code | HSL / RGB | Role |
| :--- | :--- | :--- | :--- |
| **Deep Obsidian** | #0B0E14 | HSL(222, 27%, 6%) | Primary Background / Core. |
| **Neon Cyan** | #00F5FF | HSL(182, 100%, 50%) | Active State / Success / Tiers. |
| **Toxic Orange** | #FF4500 | HSL(16, 100%, 50%) | **Hazard** / PAINS Alerts. |
| **Lead Gold** | #FFD700 | HSL(51, 100%, 50%) | High Lead Score / Metadata. |
| **Ghost Slate** | #2D3436 | HSL(192, 9%, 19%) | Card Borders / Dividers. |

---

## 3. Typography (Inter & Orbitron)

*   **Main Copy (Readability):** **Inter** (Variable). Clean, sans-serif, high legibility for small ADMET numbers.
*   **Headers (The Look):** **Orbitron** or **Roboto Mono**. High-tech, futuristic, scientific precision.

---

## 4. Iconography & Symbols (⬡)

*   **The Hexagon (⬡):** Represents the Benzene ring, the universal symbol for Chemistry. Used as the main logo and bullet point marker.
*   **The Flask (🧪):** Represents the "Physicochemical Constraint Laboratory."
*   **The Robot (🤖):** Represents the "Anthropic AI Rationale Engine."

---

## 5. UI Layout: "Glassmorphism" Philosophy

*   **Transparency:** All background cards use `rgba(45, 52, 54, 0.7)` with a `blur(10px)`.
*   **Depth:** Subtle `box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3)`.
*   **Z-Index:** High-priority "Hazard" alerts should have a glowing halo to immediately draw the eye.

---

## 6. Official Presentation Materials (MDP 2026)

*   **Master PPTX:** [ChemoFilter_COMPLETE_Presentation.pptx](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/ChemoFilter_COMPLETE_Presentation.pptx).
*   **Presentation Script:** [PRESENTATION_SCRIPT.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/PRESENTATION_SCRIPT.md).
*   **Demo Sequence:** [VIRTUAL_SCREENING_WORKFLOW.md](file:///c:/Users/Piyush%20Kumar/OneDrive/Attachments/zip%20MDP/LAST%20ONE/VIRTUAL_SCREENING_WORKFLOW.md).

---

## 7. How to Maintain Brand Consistency

When adding a new tab (e.g., Tier 11) in `app.py`:
1.  Use the `render_metric_card()` function from `chemo_ui_components.py`.
2.  Maintain the **Neon Cyan** text shadow for all mathematical result numbers.
3.  Ensure all 3D visualizations use the **Deep Obsidian** background for high-contrast molecular rendering.
