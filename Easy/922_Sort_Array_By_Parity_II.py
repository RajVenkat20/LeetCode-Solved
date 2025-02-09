class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evenPar, oddPar = 0, 1
        ans = [0] * n

        for i in range(n):
            if(nums[i] & 1):
                ans[oddPar] = nums[i]
                oddPar += 2
            else:
                ans[evenPar] = nums[i]
                evenPar += 2

        return ans