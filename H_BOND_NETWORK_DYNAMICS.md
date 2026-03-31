# ⬡ ChemoFilter: H-Bond Network Dynamics & Permeability Logic

**The Science of Hydrogen Bond Acceptors (HBA) and Donors (HBD)**  
*Predicting Passive Diffusion and Receptor Binding Affinity*

---

## 1. Overview: The Foundation of Lipinski’s Ro5

The most common reason for a drug's failure in Phase I is its inability to cross the intestinal wall or the blood-brain barrier. **Hydrogen bonding** is the single most important factor in this process. ChemoFilter utilizes the **Tier 1 (Vanguard Core)** to extract precise H-Bond counts based on the Lipinski and Veber formulations.

---

## 2. Defining HBA & HBD (RDKit Implementation)

ChemoFilter uses the `Chem.Lipinski.NumHAcceptors` and `Chem.Lipinski.NumHDonors` functions, but with an additional **Tier 5 (Omni-Science)** layer for precision:

*   **HBD (Donors):** The number of Nitrogen or Oxygen atoms with at least one attached Hydrogen. 
*   **HBA (Acceptors):** The number of Nitrogen or Oxygen atoms.
    *   *Constraint:* Lipinski rules require $HBD \le 5$ and $HBA \le 10$ for optimal oral bioavailability.

---

## 3. Beyond Simple Counts: The "Internal H-Bond" (IHB) Analysis

A common "false negative" in drug discovery is a molecule that seemingly has too many H-bonds but performs well because it forms **Internal Hydrogen Bonds** (IHBs), which "mask" its polarity and allow it to cross lipid membranes more easily.

*   **ChemoFilter Implementation:** Tier 7 (**Celestial Engine**) performs a basic structural analysis of 3D conformers to identify potential IHBs (atoms within 2.5–3.5 Å of each other).
*   **Result:** This significantly improves the accuracy of the **BOILED-Egg** model, especially for complex macrocycles.

---

## 4. TPSA vs H-Bond Counts

While HBA/HBD counts are discrete values, **TPSA (Topological Polar Surface Area)** is a continuous measure (Å²).

*   **TPSA < 140 Å²:** Generally required for good oral absorption (Veber’s rule).
*   **TPSA < 90 Å²:** Generally required for crossing the Blood-Brain Barrier (BBB).

ChemoFilter dynamically maps these two metrics against each other in the **"Physicochemical Constraint Laboratory"** tab to identify "Borderline Leads."

---

## 5. Lipophilic Efficiency (LipE) Integration

Hydrogen bonds are "energetically expensive" for a molecule to lose when crossing a membrane. To compensate, a drug often needs higher lipophilicity (LogP). ChemoFilter calculates the **LipE** (Lipophilic Efficiency) to ensure that the H-bond network is balanced against its partition coefficient.

$$LipE = pIC50 - LogP$$

---

## 6. How to Optimize Your Lead Structure

If ChemoFilter flags a molecule for **"Excessive H-Bond Polar Surface Area"**:
1.  **Methylation:** Add a methyl group to a Nitrogen to reduce H-bond donors.
2.  **Bioisosteres:** Replace a highly polar Nitrogen with a less polar Carbon or Fluorine atom while maintaining the structural scaffold.
3.  **Cyclization:** Attempt to lock the H-bonds into an internal ring structure as identified by the **Scaffold Morphing** module.
