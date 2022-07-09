# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve():
            r, c = findEmpty()
            if r == -1 and c == -1:
                return True
            for num in range(1, 10):
                if isValid(num, r, c):
                    # add value
                    board[r][c] = str(num)

                    # recursive check
                    if solve():
                        return True

                    # remove value
                    board[r][c] = "."

            return False

        def findEmpty():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        return r, c
            return -1, -1

        def isValid(num, r, c):
            return checkRow(num, r, c) and checkCol(num, r, c) and checkGrid(num, r, c)

        def checkRow(num, r, c):
            for i in range(9):
                if board[r][i] == str(num):
                    return False
            return True

        def checkCol(num, r, c):
            for i in range(9):
                if board[i][c] == str(num):
                    return False
            return True

        def checkGrid(num, r, c):
            gridRow = (r // 3) * 3
            gridCol = (c // 3) * 3

            for r in range(gridRow, gridRow + 3):
                for c in range(gridCol, gridCol + 3):
                    if board[r][c] == str(num):
                        return False
            return True

        solve()
        