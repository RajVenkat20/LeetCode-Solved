class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while(top <= bottom):
            row = (top + bottom) // 2
            if(target < matrix[row][0]):
                bottom = row - 1
            elif(target > matrix[row][-1]):
                top = row + 1
            else:
                break

        if(not (top <= bottom)):
            return False
        
        l, r = 0, cols - 1
        while(l <= r):
            mid = (l + r) // 2
            if(matrix[row][mid] > target):
                r = mid - 1
            elif(matrix[row][mid] < target):
                l = mid + 1
            else:
                return True

        return False