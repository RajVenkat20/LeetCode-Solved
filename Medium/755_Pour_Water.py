class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """
        while(volume > 0):
            left = right = k
            for i in range(k - 1, -1, -1):
                if(heights[i] < heights[left]):
                    left = i
                elif(heights[i] > heights[left]):
                    break

            if(left < k):
                heights[left] += 1
            else:
                for i in range(k + 1, len(heights)):
                    if(heights[right] > heights[i]):
                        right = i
                    elif(heights[right] < heights[i]):
                        break

            if(right > k):
                heights[right] += 1
            elif(left == right == k):
                heights[k] += 1

            volume -= 1

        return heights