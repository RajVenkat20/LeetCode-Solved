class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hm = {}

        for idx, val in enumerate(nums):
            hm[val] = idx

        print(hm)

        for curr, new in operations:
            idx = hm[curr]
            nums[idx] = new
            del hm[curr]
            hm[new] = idx
        
        return nums