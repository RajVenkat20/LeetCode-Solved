class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        tripSum = 0
        size = len(nums)

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    res = (nums[i] - nums[j]) * nums[k]
                    if(res > 0):
                        tripSum = max(tripSum, res)

        return tripSum