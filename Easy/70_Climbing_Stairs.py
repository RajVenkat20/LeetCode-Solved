class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp  = [0] * (n + 1)
        dp[n], dp[n - 1] = 1, 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]