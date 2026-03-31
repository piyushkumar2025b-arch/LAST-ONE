# ⬡ ChemoFilter: Virtual Screening Diversity Metrics

**Ensuring Chemical Space Coverage in Large-Scale Libraries**  
*The "Shannon Entropy" of Molecular Fingerprints*

---

## 1. Executive Overview

In virtual screening, the goal is often to find a lead that is not just potent but **Unique**. A "Diverse Library" contains a wide variety of chemical scaffolds, rather than 100 derivatives of the same core. **ChemoFilter** uses statistical measures to quantify the diversity of a user's collection.

---

## 2. Defining Diversity ($D$)

Diversity is the inverse of similarity. ChemoFilter measures this as the **Average Tanimoto Distance ($1 - Sim$)** among the top 100 leads.

1.  **High Diversity ($D > 0.8$):** A "Spread Out" library. High probability of finding a novel drug class.
2.  **Low Diversity ($D < 0.3$):** A "Focused" library. Likely a SAR study exploring a single structural motif.

---

## 3. Shannon Entropy of Fingerprints ($H'$)

For libraries of $1,000+$ compounds, the system calculates the **Shannon Entropy** ($H'$) across the 2,048-bit **Morgan Fingerprint BitVector**.

$$H' = -\sum_{i=1}^{n} p_i \ln(p_i)$$

*   **Logic:** $p_i$ is the probability of bit $i$ being set to 1.
*   **Result:** A higher $H'$ means the bits are distributed across the fingerprint evenly—an indicator of high structural complexity and diversity.

---

## 4. Clustering: The "K-Means" Mapping

The **"Analytical Dashboard"** tab in `app.py` includes a **Scaffold-Clustering Map**:

*   **Logic:** Compounds are clustered into groups based on structural similarity.
*   **Significance:** If a user identifies a "Potent Cluster" of 10 molecules, they can use the **Scaffold Morphing** module to explore "Hopping" to a new, diverse cluster while maintaining the same pharmacophore.

---

## 5. Visualizing Diversity: The "Chemical Cloud"

The UI features a **PCA Projection (3D Chemical Cloud)**:

*   **Logic:** High-dimensional descriptors are compressed into a 3D scatter plot.
*   **Interpretation:** A "Healthy Library" looks like a wide, dispersed cloud. A biased library looks like a single, dense point.

---

## 6. How to Improve Your Library's Diversity

If ChemoFilter flags your library as **"Low Chemical Diversity"**:
1.  **Add Fragments:** Inject common chemical fragments ($Br, F, NO2$) into the **"Scaffold Hopper"**.
2.  **Natural Product Search:** Use the **PubChem API** to search for natural structural analogs that might have higher Fsp3 complexity.
3.  **Randomized Side-Chains:** Use the **RECAP** module to randomly mutate existing leads into new structural scaffolds.
