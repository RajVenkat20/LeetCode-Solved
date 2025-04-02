class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        size = len(nums)
        left = nums[0]
        for j in range(1, size):
            if(nums[j] > left):
                left = nums[j]
            for k in range(j + 1, size):
                res = max(res, (left - nums[j]) * nums[k])

        return res