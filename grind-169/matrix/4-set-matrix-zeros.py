# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])
        
        # check first row 
        firstRowZeros = False
        for c in range(COL):
            if matrix[0][c] == 0:
                firstRowZeros = True
        
        # check first col
        firstColZeros = False
        for r in range(ROW):
            if matrix[r][0] == 0:
                firstColZeros = True
        
        # check the matrix beside the first row and col
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # process the matrix beside the first row and col
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # process the first row and the first col
        if firstRowZeros:
            for c in range(COL):
                matrix[0][c] = 0
        
        if firstColZeros:
            for r in range(ROW):
                matrix[r][0] = 0

# O(M*N)
# O(1)
        