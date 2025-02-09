class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        posIdx, negIdx = 0, 1
        ans = [0] * n

        for i in range(n):
            if(nums[i] < 0):
                ans[negIdx] = nums[i]
                negIdx += 2
            else:
                ans[posIdx] = nums[i]
                posIdx += 2

        return ans