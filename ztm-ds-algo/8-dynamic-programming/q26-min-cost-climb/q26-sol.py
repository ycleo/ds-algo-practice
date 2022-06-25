# https://leetcode.com/problems/min-cost-climbing-stairs/

# recurrence relation:
    # minCost(0) = cost[0]
    # minCost(1) = cost[1]
    # minCost(i) = cost[i] + min  { minCost(i - 1), minCost(i - 2) }

#========================================================================
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(i):
            if i <= 1:
                return cost[i]
            return cost[i] + min(minCost(i - 1), minCost(i - 2))
        
        cost = cost + [0]
        return minCost(len(cost) - 1)

# time: O(2^n)
# space: O(n)

#========================================================================
# Using DP Approach (Top Down)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]
        dp = [-1] * len(cost)
        
        def minCost(i):
            if dp[i] != -1:
                pass
            elif i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(minCost(i - 1), minCost(i - 2))
            return dp[i]

        return minCost(len(cost) - 1)

# time: O(n)
# space: O(n)

#========================================================================
# Using DP Approach (Bottome Up)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

# time: O(n)
# space: O(1)
