# https://leetcode.com/problems/knight-probability-in-chessboard/submissions/

# DP solution (Top Down)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        
        def recurse(n, k, r, c, dp):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if k == 0:
                return 1
            
            if dp[k][r][c] == 0:
                for x, y in directions:
                    dp[k][r][c] += recurse(n, k-1, r+x, c+y, dp) / 8 
            
            return dp[k][r][c]
                
        return recurse(n, k, row, column, dp)

# time: O( k * n^2 )
# space: O( k * n^2 )

# ==========================================================================================================
# DP Solution (Bottom Up) too hard!
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        prob = 0
        dp = [[0] * n for _ in range(n)] 
        nextDp = [[0] * n for _ in range(n)]
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        
        dp[row][column] = 1
        
        for _ in range(k):
            for r in range(n):
                for c in range(n):
                    for x, y in directions:
                        if n > r+x >= 0 and n > c+y >= 0: 
                            nextDp[r][c] += dp[r+x][c+y] / 8
            dp = nextDp
            nextDp = [[0] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                prob += dp[r][c]
                
        return prob

# time: O( k * n^2 )
# space: O( n^2 )
