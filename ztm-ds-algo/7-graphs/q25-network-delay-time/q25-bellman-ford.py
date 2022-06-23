# https://leetcode.com/problems/network-delay-time/

# Bellman-Ford Alog cannot be used when graph has a "negative cycle" !!!

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        table = [float('inf')] * n
        table[k - 1] = 0
        
        for _ in range(n - 1):
            changed = False
            for u, v, w in times:
                if (table[u - 1] + w) < table[v - 1]:
                    table[v - 1] = table[u - 1] + w
                    changed = True
            if changed == False:
                break
        
        return max(table) if max(table) != float('inf') else -1

# time: O(E*V)
# space: O(V)