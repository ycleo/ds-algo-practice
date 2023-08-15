
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# 1. DFS recursive solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hmap = {}
        
        def dfs(node):
            if node in hmap:
                return hmap[node]
            
            copy = Node(node.val)
            hmap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))            
            return copy
            
        return dfs(node) if node else None

# 2. DFS iterative solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        hmap, visited, stack = dict(), set(), [node]
        
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            
            if curr not in hmap:
                hmap[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                if nei not in hmap:
                    hmap[nei] = Node(nei.val)
                hmap[curr].neighbors.append(hmap[nei])
                stack.append(nei)
        
        return hmap[node]

# BFS iterative solution
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        hmap, visited, q = {}, set(), deque([node])
        
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            
            if curr not in hmap:
                hmap[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                if nei not in hmap:
                    hmap[nei] = Node(nei.val)
                hmap[curr].neighbors.append(hmap[nei])
                q.append(nei)
        
        return hmap[node]