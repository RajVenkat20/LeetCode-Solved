class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm = {0: -1}
        prefixSum = 0

        for idx, num in enumerate(nums):
            prefixSum += num

            rem = prefixSum % k
            if(rem not in hm):
                hm[rem] = idx
            elif(idx - hm[rem] > 1):
                return True

        return False