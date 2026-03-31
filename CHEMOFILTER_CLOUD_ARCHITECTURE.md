# ⬡ ChemoFilter: Cloud Deployment Architecture (Mermaid)

**Scaling "Offline-First" to "Institutional Cluster" (Phase 4 Roadmap)**  
*The Technical Blueprint for AWS / GCP / Azure Hosting*

---

## 1. Executive Overview

While ChemoFilter is designed to be **"Local-First"**, institutional environments (like VIT Chennai or a Biotech startup) will require a **Centralized Research Hub**. This document provides the high-level cloud architecture for deploying ChemoFilter as a distributed **Streamlit / Dask** cluster.

---

## 2. Cloud Architecture Diagram (Mermaid)

```mermaid
graph TD
    A[User Browser (Localhost)] --> B[Load Balancer (Nginx/Envoy)];
    B --> C1[Streamlit Instance 1];
    B --> C2[Streamlit Instance 2];
    C1 --> D{Data Engine Broker};
    C2 --> D;
    D --> E[(S3 Bucket: compounds.parquet)];
    D --> F{Dask Distributed Cluster};
    F --> G1[Worker Node (Tier 1-5)];
    F --> G2[Worker Node (Tier 7-9: GPU)];
    D --> H[Redis: Fingerprint Cache];
    C1 --> I[Anthropic / Gemini API Hub];
```

---

## 3. Component Details & Technologies

1.  **Load Balancer:** Standard Nginx or Cloud-Native (AWS ELB) handles **100+ concurrent user sessions** during the MDP presentation.
2.  **Dask Cluster:** For screening $1,000,000+$ compounds. Dask handles the distribution of RDKit C++ bindings across multiple CPU/GPU worker nodes.
3.  **S3 / Delta Lake:** The single source of truth for the **FastParquet** database. ChemoFilter utilizes **Versioning** (AWS S3) to ensure data-rollback if a screening run is interrupted.
4.  **Redis Cache:** Stores the **SHA-256 Hashed Fingerprints**. This prevents different users from performing the same $O(N^3)$ Aether Engine calculation twice.

---

## 4. Scalability Metrics (Projected Phase 4)

| User Count | CPU (Cores) | RAM (GB) | Storage (TB) | Expected Latency |
| :--- | :--- | :--- | :--- | :--- |
| **1 (Local)** | 4 | 8 | 1 | $< 1s$ |
| **10 (Research Lab)** | 32 | 128 | 5 | $< 1s$ |
| **100+ (Institutional)** | 256+ | 1,024 | 20+ | $< 1.5s$ |

---

## 5. Security: VPN & Air-Gapped Cloud

To maintain scientific IP (Intellectual Property) on the cloud:

*   **VPC Isolation:** All Streamlit instances and Dask workers are placed in a non-routable **Private Subnet**.
*   **Encrypted I/O:** Every read/write to the S3 bucket is encrypted using **KMS / AES-256**.
*   **Whitelisted Outbound:** The system only allows outbound traffic to the specific Anthropic/Gemini API endpoints, preventing data exfiltration.

---

## 6. How to Deploy the Cloud Edition

For the **VIT Chennai MDP Showcase**, we recommend the **"Container-First" (Docker Compose)** deployment method:

1.  `docker-compose up -d --build`
2.  Navigate to the defined **Route53** or **Local IP** entry point.
3.  Upload your `.env` or `secrets.toml` into the **Environment Variables** of the container.
