from typing import Any
from typing import Callable
from typing import Union
from typing import List
from typing import Iterable
from typing import Tuple
from typing import Dict

from collections import defaultdict
import itertools
import operator


class CryptoStore:
    _FUNC_ADD_STORE: Dict[Any, Callable] = {}
    _FUNC_GET_STORE: Dict[Any, Callable] = {}

    def __init__(self):
        self.store: Dict[Any, Any] = {}

    def populate_store(
        self,
        op_str: str,
        primitives: Iterable[Any],
        *args: List[Any],
        **kwargs: Dict[Any, Any]
    ) -> None:
        populate_func = CryptoStore._FUNC_ADD_STORE[op_str]
        populate_func(self.store, primitives, *args, **kwargs)

    def get_primitives_from_store(
        self, op_str: str, nr_instances: int = 1, *args, **kwargs
    ) -> List[Any]:
        retrieve_func = CryptoStore._FUNC_GET_STORE[op_str]
        primitives = retrieve_func(self.store, nr_instances, *args, **kwargs)
        return primitives