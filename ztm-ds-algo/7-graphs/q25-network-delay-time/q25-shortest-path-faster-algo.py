# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict, deque 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # declare data structures
        timeMap = [float('inf')] * n
        adjMap = defaultdict(dict)
        queue = deque([k - 1])
        
        # initialized setting
        timeMap[k - 1] = 0
        for u, v, w in times:
            adjMap[u - 1][v - 1] = w
        
        # SPFA start
        while queue:
            currNode = queue.popleft()
            for adjNode in adjMap[currNode]:
                if timeMap[currNode] + adjMap[currNode][adjNode] < timeMap[adjNode]:
                    timeMap[adjNode] = timeMap[currNode] + adjMap[currNode][adjNode]
                    queue.append(adjNode)
        
        # return answer
        return max(timeMap) if max(timeMap) < float('inf') else -1
        
# time: average -> O(E); worst -> O(E * V)
# space: O(V + E)