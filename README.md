#  POS Update Validator

A Python-based tool that automatically validates Point-of-Sale (POS) system updates, identifying pricing mismatches, missing buttons, and sync issues — built to support smoother operations and reduce customer-impacting errors after menu or price changes.

---

##  The Problem

After POS system updates (especially using Xenial), restaurants and retail locations often encounter:

- ❌ Items showing as $0.00
- ❌ Missing or broken menu buttons
- ❌ Inconsistent pricing across terminals
- ❌ Modifiers not stacking correctly

These issues delay service, frustrate staff, and damage customer trust. Manual post-update checks are time-consuming, inconsistent, and reactive.

---

##  My Solution

I developed a **POS Update Validator** that automates post-update validation by comparing the expected menu structure with the live POS data. It scans for common update failures and provides a clean, actionable report.

###  Key Features
- Scans JSON-based POS menu files
- Identifies missing prices, button mismatches, and sync failures
- Outputs a clear CLI report (optional CSV/TXT log)
- Supports local PC deployment or scheduled automatic runs
- Prototype built for real-world use in a fast-paced restaurant setting

---

##  How It Works

1. **Inputs**
   - `expected_menu.json`: Pulled from Xenial backend (or created manually)
   - `live_menu.json`: Exported from store-level POS system
2. **Comparison Logic**
   - Matches items by name or ID
   - Flags pricing mismatches, missing buttons, and $0.00 entries
3. **Output**
   - CLI summary
   - Optional text or CSV report saved in a `/logs` folder

---

## Deployment Options

### Local PC (Prototype 1)
- Runs on Windows machines with Python 3
- Configurable via Task Scheduler (e.g., run daily at 5 AM)
- Offline compatible for in-store use

### (Future) Cloud Server
- Real-time, multi-store monitoring
- Central logging, dashboards, and alerts

---

________________________________________


