
# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row, col = len(matrix), len(matrix[0])
        
        direction = 1 # 1: go right + down ; -1: go left + up
        r = 0   # the first starting row is 1  ->  0 + direction = 1
        c = -1  # the first starting col is 0  -> -1 + direction = 0
        
        while row * col > 0:
            for _ in range(col):
                c += direction
                res.append(matrix[r][c]) 
            row -= 1
            
            for _ in range(row):
                r += direction
                res.append(matrix[r][c])
            col -= 1
            
            direction *= -1 # flip the direction
        
        return res

# O(m * n)
# O(1)
