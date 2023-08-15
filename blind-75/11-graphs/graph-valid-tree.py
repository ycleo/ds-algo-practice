# approach 1: recursive DFS
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node, parent):  # return False iff cycle detected
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

# T: O(V + E)
# S: O(V + E)

# approach 2: iterative DFS


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = {0: -1}
        stack = [0]

        while stack:
            curr = stack.pop()
            for nei in adj[curr]:
                if nei == parent[curr]:
                    continue
                if nei in parent:
                    return False
                stack.append(nei)
                parent[nei] = curr

        return len(parent) == n

# T: O(V + E)
# S: O(V + E)

# approach 3: BFS


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = {0: -1}
        q = collections.deque([0])

        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                if nei == parent[curr]:
                    continue
                if nei in parent:
                    return False
                q.append(nei)
                parent[nei] = curr

        return len(parent) == n

# T: O(V + E)
# S: O(V + E)


# approach 4: Graph Theory DFS
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = set()

    def dfs(node):
        if node in seen:
            return
        seen.add(node)
        for neighbour in adj_list[node]:
            dfs(neighbour)

    dfs(0)
    return len(seen) == n


# approach 5: Union Find
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            aRoot, bRoot = find(a), find(b)
            if aRoot == bRoot:  # two ends of the edge reach the same node -> cycle detected
                return True
            if rank[aRoot] < rank[bRoot]:
                aRoot, bRoot = bRoot, aRoot

            parent[bRoot] = aRoot
            rank[aRoot] += rank[bRoot]
            return False

        for u, v in edges:
            if union(u, v):
                return False

        return True
