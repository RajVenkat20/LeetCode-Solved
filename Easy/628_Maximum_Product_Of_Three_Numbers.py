class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        potential1 = nums[0] * nums[1] * nums[-1]
        potential2 = nums[-1] * nums[-2] * nums[-3]

        return max(potential1, potential2)