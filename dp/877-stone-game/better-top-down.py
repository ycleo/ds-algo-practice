class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # list all the possible ranges of piles
        dp = [[0] * n for _ in range(n)]
        # dp[l][r]: max value that first pick player can gain in piles[l:r+1] -> find dp[0][n-1]

        def dfs(l, r) -> int:  # check the current player has bigger gain than next player
            if l > r:
                return 0
            if l == r:
                return piles[l]
            if dp[l][r] > 0:
                return dp[l][r]

            dp[l][r] = max(piles[l] - dfs(l+1, r), piles[r] - dfs(l, r-1))
            return dp[l][r]

        aliceGain = dfs(0, n-1)
        return aliceGain > 0

# TC: O(n^2)
# SC: O(n^2)
