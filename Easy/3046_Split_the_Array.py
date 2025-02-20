class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hm = {}

        for val in nums:
            hm[val] = hm.get(val, 0) + 1

            if(hm[val] > 2):
                return False

        return True