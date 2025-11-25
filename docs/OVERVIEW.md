# Law-N SQL Playground — Overview

This repo is the **“glue layer”** between:

- `law-n-signal-sim` (signal-level simulator)
- `law-n-sql-core` (N-SQL language + engine)

## Flow

1. **Simulation**
   - We use `SignalSimulator` from `law-n-signal-sim`
   - Get time-stepped snapshots of `RouteSnapshot` objects

2. **Storage**
   - We push snapshots into `NetworkRoutesStore`
   - Internally it's just a list of dicts with columns:

     - `device`
     - `channel`
     - `tower_id`
     - `frequency`
     - `g_layer`
     - `latency_ms`
     - `signal_quality`

3. **Querying**
   - Always available:
     - `.filter(py_predicate)` — simple Python predicate filtering
   - Optionally (if `law-n-sql-core` available):
     - `.query_nsql(query: str)` — pass-through to N-SQL engine

## Why This Repo Exists

- To give developers a **hands-on** way to touch Law-N ideas
- To provide **Dev.to** and GitHub with a concrete, runnable example
- To serve as a base for:
  - CLSI demos
  - N-LLM experiments
  - Tower/device OS prototypes
