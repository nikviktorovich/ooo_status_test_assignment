import dataclasses
from collections.abc import Generator
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

import tree_assignment.models as models


@dataclasses.dataclass
class TreeNode:
    id: int
    parent: Optional['TreeNode']
    children: List['TreeNode']
    item: models.Item


class TreeStore:
    nodes: Dict[int | Literal['root'], TreeNode]


    def __init__(self, items: List[models.Item]) -> None:
        self.nodes = self.parseTree(items)
    

    def parseTree(
            self,
            items: List[models.Item],
        ) -> Dict[int | Literal['root'], TreeNode]:
        nodes: Dict[int | Literal['root'], TreeNode] = {}

        for item in items:
            itemId = item['id']
            parentId = item['parent']
            parent = None if parentId == 'root' else nodes[parentId]

            node = TreeNode(id = itemId, parent=parent, children=[], item=item)

            if itemId not in nodes:
                nodes[itemId] = node

            if parentId == 'root':
                nodes[parentId] = node
            else:
                nodes[parentId].children.append(node)

        if 'root' not in nodes:
            raise ValueError('Structure has no root element')

        return nodes


    def getAll(self) -> List[models.Item]:
        root = self.nodes['root']
        all_children = [node.item for node in self._traverseChildren(root)]
        return [root.item] + all_children
    

    def _traverseChildren(self, node: TreeNode) -> Generator[TreeNode, None, None]:
        yield from node.children

        for child in node.children:
            yield from self._traverseChildren(child)
    

    def getItem(self, id: int | Literal['root']) -> Optional[models.Item]:
        node: Optional[TreeNode] = self.nodes.get(id)

        if node is None:
            return None

        return node.item
    

    def getChildren(self, id: int | Literal['root']) -> List[models.Item]:
        node = self.nodes.get(id)

        if node is None:
            return []

        return [child.item for child in node.children]
    

    def getAllParents(self, id: int | Literal['root']) -> List[models.Item]:
        node = self.nodes[id]
        return [parent.item for parent in self._traverseParents(node)]
    

    def _traverseParents(self, node: TreeNode) -> List[TreeNode]:
        currentNode: TreeNode = node
        parents: List[TreeNode] = []

        while currentNode.parent is not None:
            parents.append(currentNode.parent)
            currentNode = currentNode.parent

        return parents
