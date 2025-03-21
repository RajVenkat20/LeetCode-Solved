class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm, res = {}, []

        for val in nums1:
            hm[val] = hm.get(val, 0) + 1

        for val in nums2:
            if(val in hm):
                res.append(val)
                hm[val] -= 1
                if(hm[val] == 0):
                    hm.pop(val)
        
        return res