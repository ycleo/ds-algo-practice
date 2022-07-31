class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, ocean, prevH):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in ocean
                or heights[r][c] < prevH
            ):
                return

            ocean.add((r, c))
            for hor, ver in dirs:
                dfs(r + hor, c + ver, ocean, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)
    
        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res