# ⬡ ChemoFilter: Future Development Roadmap

The current master architecture (Version `1M` Omnipotent Build) is highly stable and configured perfectly for the VIT Chennai MDP 2026 presentation. It represents the pinnacle of 2D heuristic calculations.

However, computational chemistry constantly shifts. Here is the strict, three-phase architectural roadmap for scaling the system toward true predictive pharmacology.

---

## 🟢 PHASE 1: Current State (VIT Showcase Ready)
**Focus:** High-throughput triage, mathematical heuristics, and educational UI visibility.
*   $O(1)$ memory batch processing using `fastparquet`.
*   Complete 2D topological analytics (Lipinski, Veber, QED).
*   API integration translating complex numerical floats into narrative text using Anthropic LLMs.
*   Instantaneous 3D conformational optimization (MMFF94 force-fields).
*   Fully decoupled, React-free UI operating cleanly via Python.

## 🟡 PHASE 2: Deep Learning & Representation (Q4 2026)
**Focus:** Moving from Boolean rules (e.g., LogP < 5) to non-linear Graph Neural Networks.
1.  **PyTorch GNN Integration:** Replace the heuristic `ames_risk` and `herg_risk` functions. Instead of counting basic nitrogens, the architecture will pass the molecular graph (edges/nodes) through a pre-trained Message Passing Neural Network (MPNN) like *Chemprop* to extract true predictive toxicity probabilities.
2.  **GPU Tensor Acceleration:** Wrap `RDKit` generation vectors in `CuPy` and hand them to NVIDIA tensors. This will reduce batch times for 100,000 molecules from 3 minutes to 4 seconds.
3.  **Generative AI Design Space:** Integrate a simplified Diffusion Model. Instead of the user providing SMILES, the user defines "Target hERG: Low, Target LogP: 2.5", and the AI hallucinates valid SMILES strings in real-time.

## 🔴 PHASE 3: Quantum Mechanics & DFT Limits (2027+)
**Focus:** Physics approximations.
1.  **PSI4 Wrapper Generation:** Sub-process calling to local or cloud-based `PSI4` instances to execute real Density Functional Theory (DFT) calculations.
2.  **HOMO/LUMO Orbital Plotting:** Calculate exact HOMO (Highest Occupied Molecular Orbital) energies. Provide quantitative prediction of reactivity and phototoxicity—impossible with current topological rules.
3.  **Protein-Ligand Docking Pipeline:** Currently, the system floats without a target protein. Phase 3 involves accepting a `.PDB` file from AlphaFold, mapping the binding pocket, and executing local *AutoDock Vina* structural scoring directly in the browser.

---
*The transition to Phase 2 limits immediate hardware accessibility. Therefore, the Phase 1 Rule-Based system will remain indefinitely preserved as the "Vanguard Core" for offline operations where VRAM is unavailable.*
