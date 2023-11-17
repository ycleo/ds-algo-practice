class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # list all the possible ranges of piles
        dp = [[0] * n for _ in range(n)]
        # dp[l][r]: max value that first pick player can gain in piles[l:r+1] -> find dp[0][n-1]

        for i in range(n):
            dp[i][i] = piles[i]

        for rangeSize in range(2, n+1):
            for l in range(n-rangeSize+1):
                r = l + rangeSize - 1
                dp[l][r] = max(piles[l] - dp[l+1][r], piles[r] - dp[l][r-1])

        return dp[0][n-1]

# TC: O(n^2)
# SC: O(n^2)
