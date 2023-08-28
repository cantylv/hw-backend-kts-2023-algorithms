from typing import Any
from collections import deque


__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:

    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = []
        self._dfs_recursive(self._root, visited)
        return visited

    def _dfs_recursive(self, node, visited):
        if node not in visited:
            visited.append(node)
            for neighbor in node.outbound:
                self._dfs_recursive(neighbor, visited)

    def bfs(self) -> list[Node]:
        visited = []
        queue = deque([self._root])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                queue.extend(neighbor for neighbor in node.outbound if neighbor not in visited)
        return visited






