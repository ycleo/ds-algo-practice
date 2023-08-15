# approach 1: topological sort + BFS

# ["wrt","wrf","er","ett","rftt"]
# adjList:
# t -> f
# w -> e
# r -> t
# e -> r

# topological sort (BFS)
# w -> e -> r -> t -> f

# be careful about the edge case: all chars > '',  ex: "abc" > "ab"
# if there is an input like ["abc", "ab"], aka w2 is the prefix of w1
# we cannot decide the final order for 'c'
import collections


class Solution:
    def alienOrder(self, words) -> str:
        adj = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for w in words:
            for c in w:
                indegree[c] = 0

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            p = 0
            while p < len(w1) and p < len(w2):
                if w1[p] != w2[p]:
                    adj[w1[p]].append(w2[p])
                    indegree[w2[p]] += 1
                    break
                p += 1

            # handle edge case
            if len(w1) > len(w2) and p == len(w2):
                return ""

        q = collections.deque()
        for c, indeg in indegree.items():
            if indeg == 0:
                q.append(c)

        topoOrder = ""
        while q:
            c = q.popleft()
            topoOrder += c
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return topoOrder if len(topoOrder) == len(indegree) else ""

# T: O(total number of chars)
# S: O(total number of distinct chars)
