class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minimal = float('inf')

        for i in range(len(prices)):
            if(minimal > prices[i]):
                minimal = prices[i]
            maxProfit = max(maxProfit, prices[i] - minimal)

        return maxProfit