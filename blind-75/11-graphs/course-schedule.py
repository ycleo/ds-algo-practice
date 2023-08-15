# approach 1: directed graph DFS
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visited = {}  # node -> 'seen' or 'processed'

        def dfs(crs):  # return False iff detect cycle
            if crs in visited:
                return visited[crs] == "processed"
            visited[crs] = "seen"
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visited[crs] = "processed"
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

# time: O(n + p)
# n: numCourses, p: len(prerequisites)


# approach 2: topological sort (BFS)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
            indegree[pre] += 1

        q = collections.deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        courseOrder = []
        while q:
            curr = q.popleft()
            courseOrder.append(curr)
            for nei in adjList[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        print(courseOrder)
        return len(courseOrder) == numCourses

# T: O(n + p)
# S: O(n + p)
