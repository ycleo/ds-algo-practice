# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        def swap(r1, c1, r2, c2):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        
        # transpose
        for r in range(n):
            for c in range(r + 1, n):
                swap(r, c, c, r)
        
        # reverse
        for r in range(n):
            for c in range(n // 2):
                swap(r, c, r, -c-1)
