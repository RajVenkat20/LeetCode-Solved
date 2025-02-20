class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if(b in hm):
                return [i, hm[b]]
            hm[a] = i     