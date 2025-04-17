class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}

        for i, num in enumerate(nums):
            if(num not in left):
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        maxDegree = max(count.values())

        for x in count:
            if(count[x] == maxDegree):
                ans = min(ans, right[x] - left[x] + 1)

        return ans