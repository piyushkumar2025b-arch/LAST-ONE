# ⬡ ChemoFilter: Ethics & Chemical Safety Compliance

In computational drug-discovery and AI-augmented chemistry, the dual-use nature of generative models and topological mapping poses severe bio-security risks. This document explicitely defines our ethical boundaries.

---

## 1. The Dual-Use Dilemma
The exact same heuristic algorithms that predict high Blood-Brain Barrier (BBB) penetration and high stability for severe neurological drugs can be inverted to design highly stable, highly penetrant neurotoxins.
If the `LeadScore` algorithm is optimised purely for target affinity, ignoring toxicity, it becomes a weaponisation engine.

## 2. Hardcoded Toxicity Rejection
To prevent dual-use exploitation, `chemo_scoring.py` possesses asymmetrical hardcoded rejection constraints that **cannot be bypassed via the UI**:
1.  **Chemical Warfare Agents (CWAs):** The engine aggressively flags and zeroes out scores for organophosphate nerve agent topological markers (e.g., specific `P-F` or `P-S` bonds matching Sarin/VX subclasses).
2.  **Zero-Tolerance Lethality Alarms:** If the `ames_risk` or `herg_risk` trigger `HIGH / Likely Mutagen`, the mathematical engine artificially suppresses the `Lead_Score` to $0$, even if the target affinity is perfect.
3.  **No Optimization of Poisons:** The AI Explainer tab (`Anthropic Claude`) is system-prompted natively to refuse the structural optimization of known poisons, toxophores, or DEA Schedule I synthetic precursors. 

## 3. Data Privacy (Proprietary IPs)
Under ethical guidelines regarding intellectual property logic (Phase 1 Trials):
*   No `.CSV` data uploaded by researchers is recorded, logged, or sent to a telemetry server. 
*   The `jsonl` WAL buffer is strictly local, ensuring that if a rival researcher uses this app, their SMILES remain isolated to their machine's local disk cache.

## 4. Limitation of Medical Liability
ChemoFilter is an **Academic Research Platform**, strictly bounded to topological heuristics and early-stage lead filtering. 
It does **NOT** constitute medical authorization, nor does it override *in-vitro* or *in-vivo* clinical testing. The `Grade: A` designation means a molecule maps cleanly to Lipinski/Veber rules; it does not mean it is safe for mammalian consumption.
