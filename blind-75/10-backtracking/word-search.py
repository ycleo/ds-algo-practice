class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0 
                or r >= ROWS 
                or c >= COLS
                or board[r][c] == "#"
                or board[r][c] != word[i] 
            ):
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"
            res = (
                dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
            )
            board[r][c] = tmp
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
    
# time: O(R * C * 4^n)
# 4 directions