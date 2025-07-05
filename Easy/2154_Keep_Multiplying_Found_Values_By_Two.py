class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hm = set(nums)

        while(original in hm):
            original *= 2

        return original