"""
law_n_sql_playground

End-to-end Law-N playground:
- Run signal simulation
- Store network.routes
- Query via Python or N-SQL (if available).
"""

from .datastore import NetworkRoutesStore
from .playground import run_basic_demo

__all__ = ["NetworkRoutesStore", "run_basic_demo"]
