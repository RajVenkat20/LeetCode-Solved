class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        size = len(nums)

        for i in range(size):
            val = abs(nums[i - 1])
            if(nums[val - 1] >= 0):
                nums[val - 1] *= -1
            else:
                res.append(val)

        return res