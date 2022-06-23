# https://leetcode.com/problems/network-delay-time/

# Dikstra Algo cannot be used when graph has a "negative edge" !!!
import heapq
from collections import defaultdict 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # declare data structures
        timeMap = {}
        adjMap = defaultdict(list)
        pQueue = [[0, k]]
        
        # complete adjacency map recoards  # O(E)
        for u, v, w in times:
            adjMap[u].append([v, w])
            
        # Dijkstra's Algo
        while pQueue: 
            currTime, currNode = heapq.heappop(pQueue) 
            
            if currNode not in timeMap:
                timeMap[currNode] = currTime
                for v, w in adjMap[currNode]: 
                    heapq.heappush(pQueue, [currTime + w, v]) # O(logE)
            
        # return result
        return max(timeMap.values()) if len(timeMap) == n else -1

# time: O(E * logE)  Every edges will only went through once
# space: O(E + V)


