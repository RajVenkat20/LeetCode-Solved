class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(matrix, m, n, result, r, c, dr, dc):
            if(m == 0 or n== 0):
                return 

            for i in range(n):
                r = r + dr
                c = c + dc
                result.append(matrix[r][c])      
        
            spiral(matrix, n, m - 1, result, r, c, dc, -dr)
        
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        spiral(matrix, rows, cols, res, 0, -1, 0, 1)       

        return res