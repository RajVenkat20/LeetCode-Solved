class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hm = {}
        count = 0

        for i in nums:
            count += hm.get(i + k, 0) + hm.get(i - k, 0)
            hm[i] = hm.get(i, 0) + 1
            
        return count