class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm, cnt, prefSum = {}, 0, 0
        hm[0] = 1

        for i in range(len(nums)):
            prefSum += nums[i]

            if(prefSum - k in hm):
                cnt += hm[prefSum - k]

            hm[prefSum] = hm.get(prefSum, 0) + 1

        return cnt