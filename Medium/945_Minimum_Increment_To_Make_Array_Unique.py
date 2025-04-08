class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0

        for i in range(1, len(nums)):
            if(nums[i] <= nums[i - 1]):
                newValue = nums[i - 1] + 1
                cnt += newValue - nums[i]
                nums[i] = newValue

        return cnt