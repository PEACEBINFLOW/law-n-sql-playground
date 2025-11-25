from __future__ import annotations
from typing import List, Dict, Any


def filter_fast_5g(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Python-side demo filter:
    - g_layer = '5G'
    - latency_ms < 40
    """
    return [
        r for r in rows
        if r.get("g_layer") == "5G" and float(r.get("latency_ms", 9999)) < 40.0
    ]


DEMO_NSQL_QUERY = """
SELECT device, tower_id, latency_ms, signal_quality
FROM network.routes
WHERE g_layer = '5G'
  AND signal_quality > 0.9;
""".strip()
