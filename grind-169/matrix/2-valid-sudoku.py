# https://leetcode.com/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = {i: set() for i in range(9)}
        col_check = {i: set() for i in range(9)}
        grid_check = {i: set() for i in range(9)}
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                grid = (r // 3) * 3 + (c // 3)
                if num in row_check[r] or num in col_check[c] or num in grid_check[grid]:
                    return False
                row_check[r].add(num)
                col_check[c].add(num)
                grid_check[grid].add(num)
        
        return True

# O(9 * 9)
# O(3 * 9 * 9)
