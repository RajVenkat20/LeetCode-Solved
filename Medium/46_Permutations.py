class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 0):
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, nums[0])
                res.append(pCopy)

        return res