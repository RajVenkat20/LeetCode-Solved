class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestInc = 1
        longestDec = 1
        size = len(nums)

        inc = 1
        dec = 1
        for i in range(1, size):
            if(nums[i - 1] < nums[i]):
                inc += 1
                dec = 1
                longestInc = max(longestInc, inc)
            elif(nums[i - 1] > nums[i]):
                dec += 1
                inc = 1
                longestDec = max(longestDec, dec)
            else:
                inc = dec = 1

        return max(longestInc, longestDec)