class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for i in hm:
            if(hm[i] % 2 != 0):
                return False
        
        return True