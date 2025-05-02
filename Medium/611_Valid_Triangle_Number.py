class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        size = len(nums)
        for i in range(size - 1, 1, -1):
            c = nums[i]
            start = 0
            end = i - 1
            while(start < end):
                if(nums[start] + nums[end] > c):
                    ans += (end - start)
                    end -= 1
                else:
                    start += 1

        return ans