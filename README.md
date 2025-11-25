# Law-N SQL Playground (`law-n-sql-playground`)

End-to-end **Law-N playground** that:

- Uses `law-n-signal-sim` to generate synthetic `network.routes` snapshots
- Stores them in an in-memory table
- Lets you run:
  - **Python predicate queries** (always available)
  - Optional **N-SQL queries** via `law-n-sql-core` (if installed)

This is the repo that turns the abstract Law-N concepts into something you can **actually run and see**.

---

## 🚀 Quickstart

### Requirements

- Python **3.10+**
- Recommended (but optional):
  - [`law-n-signal-sim`](https://github.com/YOUR_USER/law-n-signal-sim)
  - [`law-n-sql-core`](https://github.com/YOUR_USER/law-n-sql-core)

### Install (local dev)

```bash
git clone https://github.com/YOUR_USER/law-n-sql-playground.git
cd law-n-sql-playground
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
