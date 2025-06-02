
# 📘 Strategy Tuner Dev Process & Deployment Checklist

---

### 🔄 Versioning Convention

| Suffix          | Meaning                               | Deployment Status |
| --------------- | ------------------------------------- | ----------------- |
| `_FULL_UI`      | Complete UI + logic, production-ready | Yes               |
| `_SANITIZED`    | Trimmed version for debugging/test    | No                |
| `_EXPERIMENTAL` | Experimental feature, unvalidated     | No                |
| `_vX.Y`         | Version tag (semantic)                | Conditional       |

#### Example:

- `strategy_tuner_FULL_UI_v1.3.py` → Production ready
- `strategy_tuner_EXPERIMENTAL_hmm.py` → Feature test only

---

### 📂 GitHub Branching Workflow

| Branch  | Purpose                                  |
| ------- | ---------------------------------------- |
| `main`  | Always working, deployed to Streamlit    |
| `dev`   | Feature additions and logic improvements |
| `debug` | Minimal builds for bug isolation         |

#### Tips:

- Always PR to `main` from `dev` only after UI + performance confirmed
- Do not push direct edits to `main`

---

### ✅ Deployment Checklist

Before committing to `main` or deploying to Streamlit:

- [x] All sliders and UI render
- [x] Graph displays equity vs. buy & hold
- [x] Trade log and performance metrics present
- [x] No future leakage (when testing causal mode)
- [x] Slippage, commissions functional
- [x] Strategy logic modularized (can be tested or extracted independently)
- [x] Compatible with Streamlit and local execution
- [x] Inputs validated for invalid tickers, small datasets
- [x] Simulations produce consistent results across notebook and app

🟡 Starting with v5, we are now also:

- [ ] Simulating step-by-step live equity curves
- [ ] Using forward-walking HMM regime labeling
- [ ] Applying rolling windows for Hurst/Spectral
- [ ] Validating realistic execution (slippage, spread, order lag)

---

### 📁 Local Snapshot Policy

- Save a `.zip` of each working build before changes:
  - `py`, `ipynb`, and any support files
  - Include commit message or changelog text file inside
- Optional: Timestamped file name like `snapshot_FULL_UI_2025-06-01.zip`

---

### 📄 Optional GitHub Issue Template

```
## Strategy Update Request

**Feature**: [e.g. Add volatility targeting toggle]
**File Version**: strategy_tuner_FULL_UI_v1.3.py
**Branch**: dev

### Description
Add volatility targeting input and adjust trade logic for per-regime application.

### Checklist
- [ ] Added slider
- [ ] Integrated into regime filter
- [ ] Backtest passes basic Sharpe > 0.5
- [ ] UI tested
```

---

This process keeps innovation flowing while protecting production stability.
