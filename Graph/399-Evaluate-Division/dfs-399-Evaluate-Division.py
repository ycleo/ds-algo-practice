from collections import defaultdict


class Solution:
    def getPath(self, graph, start, end, path, visited):
        if start not in graph or start in visited:
            return -1.0

        if start == end:
            return path

        visited.add(start)
        neighbors = graph[start]
        for nei, val in neighbors:
            tempPath = self.getPath(graph, nei, end, path * val, visited)
            if tempPath != -1.0:
                return tempPath
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        graph = defaultdict(list)
        for equation, val in zip(equations, values):
            end, start = equation
            graph[start].append([end, val])
            graph[end].append([start, 1.0/val])

        for q in queries:
            visited = set()
            end, start = q
            res.append(self.getPath(graph, start, end, 1, visited))

        return res


# O(N * q)
# O(N)
