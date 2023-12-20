from typing import Any
from typing import Literal
from typing import Optional
from typing import TypedDict


class ItemBase(TypedDict):
    id: int
    parent: int | Literal['root']


class Item(ItemBase, total=False):
    type: Optional[Any]
