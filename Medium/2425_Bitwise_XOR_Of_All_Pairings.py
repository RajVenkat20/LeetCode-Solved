class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        hm = {}

        for num in nums1:
            hm[num] = hm.get(num, 0) + n

        for num in nums2:
            hm[num] = hm.get(num, 0) + m
        
        ans = 0
        for key in hm:
            if(hm[key] % 2):
                ans ^= key

        return ans