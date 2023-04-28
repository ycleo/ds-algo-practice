# set a max_profit = 0
# set curr_lowest = prices[0]
# loop through the prices
# for each iteration
# if price < curr_lowest -> update curr_lowest
# else -> calculate and update max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_lowest = prices[0]

        for p in prices:
            if p < curr_lowest:
                curr_lowest = p
            else:
                max_profit = max(max_profit, p - curr_lowest)

        return max_profit


# O(N)
# O(1)
