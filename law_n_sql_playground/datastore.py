from __future__ import annotations
from typing import Any, Callable, Dict, Iterable, List, Optional

from law_n_signal_sim.models import RouteSnapshot


class NetworkRoutesStore:
    """
    Simple in-memory store for Law-N `network.routes` rows.

    Internally: a list[dict].
    """

    def __init__(self) -> None:
        self._rows: List[Dict[str, Any]] = []

        # optional: N-SQL engine, if available
        self._nsql_engine = self._try_load_nsql_engine()

    @property
    def rows(self) -> List[Dict[str, Any]]:
        return list(self._rows)

    def add_snapshots(self, snapshots: Iterable[RouteSnapshot]) -> None:
        for snap in snapshots:
            self._rows.append(snap.to_dict())

    def filter(self, predicate: Callable[[Dict[str, Any]], bool]) -> List[Dict[str, Any]]:
        """
        Python-level filtering. Always available.
        """
        return [row for row in self._rows if predicate(row)]

    # --- N-SQL integration -------------------------------------------------

    def _try_load_nsql_engine(self):
        """
        Best-effort attempt to import an N-SQL engine from `law_n_sql_core`.

        You can customize this based on how you implement the core.
        """
        try:
            # Adjust this to your actual engine API.
            # Example assumption:
            # from law_n_sql_core.engine import execute_query
            from law_n_sql_core.engine import execute_query  # type: ignore
            return execute_query
        except Exception:
            return None

    def has_nsql(self) -> bool:
        return self._nsql_engine is not None

    def query_nsql(self, query: str) -> Optional[List[Dict[str, Any]]]:
        """
        If N-SQL engine is available, pass the query and rows to it.
        Otherwise, return None.
        """
        if not self._nsql_engine:
            return None

        # The exact format may differ depending on your engine implementation.
        # Here we assume:
        #   result = execute_query(query, tables={"network.routes": self._rows})
        engine = self._nsql_engine
        result = engine(query, tables={"network.routes": self._rows})  # type: ignore[arg-type]
        return result
