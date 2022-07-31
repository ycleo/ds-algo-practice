from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == "0"
            ):
                return
            
            grid[r][c] = "0"
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for hor, ver in dirs:
                dfs(r + hor, c + ver)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
# time: O(m * n)
# space: O(max(m, n))