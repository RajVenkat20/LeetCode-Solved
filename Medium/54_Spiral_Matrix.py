class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        left, right = 0, cols - 1
        top, bottom = 0, rows - 1

        while(top <= bottom and left <= right):
            # Performing the right direction
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Performing the down direction
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Performing the left direction
            if(top <= bottom):
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if(left <= right):
                # Performing the top direction
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans