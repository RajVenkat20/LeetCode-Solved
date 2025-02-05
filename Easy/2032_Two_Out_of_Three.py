class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        c = set(nums3)

        res = list(a & b | b & c | a & c)

        return res