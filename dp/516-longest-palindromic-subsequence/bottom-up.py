class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # template: outer loop is "size", inner loop is "starting point"
        for winLen in range(1, n + 1):
            for i in range(n - winLen + 1):
                j = i + winLen - 1
                if winLen == 1:
                    dp[i][i] = 1
                    continue

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][n-1]

# s: XX i [XXX] j XXX

# TC: O(n^2)
# SC: O(n^2)
