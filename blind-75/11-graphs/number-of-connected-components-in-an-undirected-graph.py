# approach 1: Union Find
import collections


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.ret = n
        parent = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            aRoot, bRoot = find(a), find(b)
            if aRoot == bRoot:
                return
            self.ret -= 1

            if rank[aRoot] > rank[bRoot]:
                aRoot, bRoot = bRoot, aRoot
            parent[bRoot] = aRoot
            rank[aRoot] += rank[bRoot]

        for u, v in edges:
            union(u, v)

        return self.ret

# T: O(V + E)
# S: O(V)

# approach 2: Recursive DFS


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        ret = 0
        for node in range(n):
            if node not in visited:
                ret += 1
                dfs(node)

        return ret

# approach 3: iterative DFS


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(stack):
            while stack:
                curr = stack.pop()
                visited.add(curr)
                for nei in adj[curr]:
                    if nei in visited:
                        continue
                    stack.append(nei)

        ret = 0
        for node in range(n):
            if node not in visited:
                ret += 1
                dfs([node])

        return ret

# T: O(V + E) 
# Building the adjacency list will take O(E) operations, as we iterate over the list of edges once, and insert each edge into two lists. 
# During the DFS traversal, each vertex will only be visited once. This is because we mark each vertex as visited as soon as we see it, and then we only visit vertices that are not marked as visited. In addition, when we iterate over the edge list of each vertex, we look at each edge once. So total cost O(V + E)

# S: O(V + E)
