"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        new_adj_lst = []

        if not node:
            return None

        if not node.neighbors:
            return Node()

        queue = deque()
        visited[node] = Node(node.val)
        queue.append(node)

        while len(queue) > 0:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])

        return visited[node]
        
                    

            
        
        