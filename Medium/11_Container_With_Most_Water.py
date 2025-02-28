class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = float('-inf')

        while(l < r):
            breadth = min(height[l], height[r])
            length = r - l
            area = max(area, length * breadth)

            if(height[l] >= height[r]):
                r -= 1
            else:
                l += 1

        return area