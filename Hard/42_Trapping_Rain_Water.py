class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if(not height):
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while(l < r):
            if(maxL < maxR):
                l += 1 
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res