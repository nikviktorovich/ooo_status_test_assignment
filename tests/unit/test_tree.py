from typing import List

from tree_assignment import models
from tree_assignment import tree


def test_get_all_successfully():
    items: List[models.Item] = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]
    tree_instance = tree.TreeStore(items)

    items_from_tree = tree_instance.getAll()

    assert items_from_tree == items


def test_get_item_existing_item():
    items: List[models.Item] = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]
    tree_instance = tree.TreeStore(items)

    item = tree_instance.getItem(id=7)

    assert item == {"id": 7, "parent": 4, "type": None}


def test_get_children():
    items: List[models.Item] = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]
    tree_instance = tree.TreeStore(items)

    children_of_item_4 = tree_instance.getChildren(id=4)
    children_of_item_5 = tree_instance.getChildren(id=5)

    assert children_of_item_4 == [
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type" :None},
    ]
    assert children_of_item_5 == []


def test_get_all_parents():
    items: List[models.Item] = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]
    tree_instance = tree.TreeStore(items)

    parents_of_item_7 = tree_instance.getAllParents(id=7)

    assert parents_of_item_7 == [
        {"id":4, "parent":2, "type":"test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"},
    ]
