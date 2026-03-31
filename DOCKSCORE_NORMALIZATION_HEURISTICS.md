# ⬡ ChemoFilter: DockScore Normalization Heuristics

**Standardizing Binding Affinities Across Different Target Pockets**  
*The Mathematics of Identifying "High Affinity" Leads*

---

## 1. Executive Overview

Molecular docking (e.g., via AutoDock Vina) gives a **$\Delta G$ (Gibbs Free Energy)** value in $kcal/mol$. However, a $-8.0$ in a small, hydrophobic pocket is not the same as a $-8.0$ in a large, polar one. **ChemoFilter** uses normalization heuristics to make these values comparable across different targets.

---

## 2. Ligand Efficiency (LE)

The most common primary normalization. A large molecule will often have a better docking score simply because it has more atoms interacting with the protein.

$$LE = 1.37 \cdot \frac{-\Delta G}{N_{heavy}}$$

*   **Logic:** $N_{heavy}$ is the number of non-hydrogen atoms.
*   **Ideal LE Range:** $> 0.3 \space kcal \cdot mol^{-1} \cdot atom^{-1}$ is considered a "high-quality" lead.

---

## 3. Surface Area Normalization (PSA-LE)

To correct for large, polar molecules that gain energy through non-specific electrostatic interactions:

*   **Logic:** Divide the docking score by the **TPSA** (Topological Polar Surface Area).
*   **Result:** This identifies "Surgical Binders"—molecules that achieve high affinity through specific H-bonds rather than "Greedy Polarity."

---

## 4. Normalizing Across Target Classes

Comparing a **Kinase** lead with a **GPCR** lead:

| Target Class | Expected $\Delta G$ | Normalization Strategy |
| :--- | :--- | :--- |
| **Kinases** | $-7$ to $-12$ | LE-correction for large scaffolds. |
| **Ion Channels** | $-6$ to $-9$ | Charge-density normalization. |
| **GPCRs** | $-8$ to $-13$ | Entropy-penalty for flexible chains. |

---

## 5. Visualizing Normalization: The "Heat-of-Binding" Plot

The UI features a **"Heat-of-Binding Map"** (Tier 9) where:

1.  **X-Axis:** Raw Docking Score ($kcal/mol$).
2.  **Y-Axis:** Ligand Efficiency ($LE$).
3.  **The "Sweep-Spot":** The upper-left corner of the plot indicates molecules with high affinity and high efficiency. 

---

## 6. How to Extend This Heuristic

Phase 5 Roadmap involves **FEP (Free-Energy Perturbation)** docking, which uses quantum mechanics to calculate exact binding constants ($K_d$), removing the need for heuristic normalization entirely.
