# https://leetcode.com/problems/gas-station

# gas  = [1, 1, 2, 3, 4, 5]
# cost = [1, 3, 4, 5, 1, 2]
#         0, -2 -2 -2 3  6

# if total gas - total cost < 0 --> return -1
# accum = 0
# res = 0
# loop through the gas and cost array
#   accum += (gas[i] - cost[i])
#   if accum < 0:
#      accum = 0
#      res = i + 1

# return res if res < len(gas) else -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        res, accum = 0, 0
        for i in range(len(gas)):
            accum += (gas[i] - cost[i])
            if accum < 0:
                accum = 0
                res = i + 1

        return res if res < len(gas) else -1

# O(N)
# O(1)
