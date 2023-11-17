class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # dp[l][r]: longest palindrome subsequence length in s[l:r+1] -> find dp[0][n-1]

        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] > 0:
                return dp[l][r]
            if l == r:
                dp[l][r] = 1
                return 1

            if s[l] == s[r]:
                dp[l][r] = dfs(l+1, r-1) + 2
            else:
                dp[l][r] = max(dfs(l+1, r), dfs(l, r-1))

            return dp[l][r]

        return dfs(0, n-1)

# TC: O(n^2)
# SC: O(n^2)
