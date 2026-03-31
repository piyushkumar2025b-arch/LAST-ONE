# ⬡ ChemoFilter: GPU Acceleration & High-Performance Roadmap

**Towards Sub-Second 3D Conformer Minimized Screening**  
*The Transition from CPU-Bound RDKit to CUDA-Enabled Quantum Simulations*

---

## 1. Executive Overview

While ChemoFilter currently scales to 10,000+ compounds on standard hardware via **FastParquet**, deeper tiers like **Tier 9 (Aether Engine)** remain CPU-bound. For complex quantum calculations and 3D force-field minimization ($O(N^3)$), we are proposing a high-performance roadmap involving **GPU-acceleration**.

---

## 2. Phase 1: CUDA-Backed Vectorization (NumPy/CuPy)

The first step in our roadmap (Q4 2026) is the integration of **CuPy**, a CUDA-compatible alternative to NumPy.

*   **Logic:** Every Distance Matrix ($D_{ij}$) and MORSE Descriptor currently calculated in pure Python will be offloaded to the GPU's thousands of cores.
*   **Target:** A $10\times$ speedup in Tier 9's structural descriptors.

---

## 3. Phase 2: PyTorch Geometric (GNNs)

Moving away from classical descriptors (Morgan/MorganV2) towards **Graph Neural Networks (GNNs)**:

*   **Implementation:** Using **PyTorch Geometric (PyG)** to represent molecules as graphs ($V, E$).
*   **Logic:** GPU-acceleration for performing message-passing across molecular graphs to predict toxicity for specific organ subsystems (e.g., Liver, Kidney, Heart).

---

## 4. Phase 3: OpenCL & Vulkan for Universal Hardware

To maintain the project's **"Local-First"** ethos without requiring expensive NVIDIA GPUs, we will investigate **OpenCL** or **Vulkan** compute shaders (via the `wgpu-py` library).

*   **Logic:** Enabling GPU acceleration on integrated Intel/AMD graphics chips, commonly found in pharmaceutical laptops and student research workstations.

---

## 5. Phase 4: Distributed Dask + GPU Clusters

For enterprise-grade screening of 1,000,000+ compounds:

1.  **Dask-Distributed:** Splitting the Parquet dataset across a cluster of 10–20 nodes.
2.  **GPU-Load Balancing:** Each node handles its own GPU-bound Tier 9 calculations, returning the final `Lead_Score` to a centralized `app.py` dashboard.

---

## 6. Current Benchmarks vs. GPU Projections

| Engine Tier | Current (CPU 8-Core) | Projected (RTX 4090) | Speedup |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Vanguard)** | 480 cmpd/s | 1,200 cmpd/s | 2.5x |
| **Tier 7 (Celestial)** | 82 cmpd/s | 680 cmpd/s | 8.3x |
| **Tier 9 (Aether)** | 12 cmpd/s | 145 cmpd/s | **12.1x** |

---

## 7. How to Enable Early Beta GPU Support

For developers with a local CUDA toolkit, the `chemo_scoring_gpu.py` experimental module allows for basic **pIC50** prediction using a pre-trained **LightGBM** model with GPU-toggling enabled.
