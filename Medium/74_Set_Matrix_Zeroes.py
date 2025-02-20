class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeroR = []
        zeroC = []

        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j] == 0):
                    zeroR.append(i)
                    zeroC.append(j)

        for i in zeroR:
            for j in range(cols):
                matrix[i][j] = 0
        
        for j in zeroC:
            for i in range(rows):
                matrix[i][j] = 0            