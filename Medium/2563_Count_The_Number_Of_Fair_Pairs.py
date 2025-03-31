class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def countPairs(target):
            cnt = 0
            i, j = 0, len(nums) - 1

            for i in range(len(nums)):
                while(i < j and nums[i] + nums[j] > target):
                    j -= 1
                
                cnt += max(0, j - i)

            return cnt

        lowerCnt = countPairs(lower - 1)
        upperCnt = countPairs(upper)

        return upperCnt - lowerCnt