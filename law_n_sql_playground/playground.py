from __future__ import annotations
from typing import Optional

from law_n_signal_sim.simulator import SignalSimulator
from .datastore import NetworkRoutesStore
from .queries import filter_fast_5g, DEMO_NSQL_QUERY


def run_basic_demo(steps: int = 5, devices: int = 5, seed: Optional[int] = None) -> None:
    """
    1. Run the signal simulator
    2. Store routes in memory
    3. Show:
       - total rows
       - first 5 rows
       - filtered 5G < 40ms
       - optional N-SQL demo
    """
    print(f"[law-n] Simulating {steps} timesteps with {devices} devices...")

    sim = SignalSimulator(seed=seed)
    # adjust device count if using default topology
    if devices != len(sim.devices):
        from law_n_signal_sim.topology import default_devices
        sim.devices = default_devices(num_devices=devices)

    store = NetworkRoutesStore()

    for t, snapshots in sim.run(steps=steps):
        store.add_snapshots(snapshots)

    all_rows = store.rows
    print(f"\n[law-n] Total routes stored: {len(all_rows)}\n")

    # show first 5
    print("[demo] First 5 rows:")
    for row in all_rows[:5]:
        print(row)
    print()

    # python filter demo
    fast_5g = filter_fast_5g(all_rows)
    print(f"[demo] Filter: g_layer = '5G' and latency < 40ms → {len(fast_5g)} rows\n")

    # N-SQL demo
    if store.has_nsql():
        print("[demo] N-SQL engine detected. Running demo query:\n")
        print(DEMO_NSQL_QUERY)
        print()
        result = store.query_nsql(DEMO_NSQL_QUERY) or []
        print(f"[demo] N-SQL returned {len(result)} rows:")
        for row in result[:10]:
            print(row)
    else:
        print("[demo] N-SQL engine not installed. Skipping N-SQL demo.")
        print("       (Install `law-n-sql-core` and wire its engine in `datastore.py`.)")
