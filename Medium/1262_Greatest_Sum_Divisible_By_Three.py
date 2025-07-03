class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]

        for num in nums:
            for i in dp[:]:
                idx = (i + num) % 3
                dp[idx] = max(dp[idx], i + num)

        return dp[0]