# solution 1.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r - 1 < 0:
                    dp[r][c] = dp[r][c - 1]
                elif c - 1 < 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        return dp[m - 1][n - 1]

# time: O(m * n)
# space: O(m * n)

# solution 2.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(1, n):
                newRow[j] = newRow[j - 1] + row[j]
            row = newRow
        return row[-1]