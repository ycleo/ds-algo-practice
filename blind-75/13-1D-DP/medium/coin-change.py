class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("Inf")
        dp = [0] + [MAX] * amount
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[-1] if dp[-1] != MAX else -1
    
# time: O(amout * len(coins))
# space: O(amount)