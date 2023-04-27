class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        res = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
                
        return res
# time: O(n)
# space: O(1)