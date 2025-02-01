class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        size = len(nums)
        
        if(size == 1):
            return True
        
        for i in range(size - 1):
            x = nums[i] & 1
            y = nums[i + 1] & 1
            print(x, y)
            if(x == y):
                return False
             
        return True