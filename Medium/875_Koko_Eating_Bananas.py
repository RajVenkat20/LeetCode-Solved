import math

class Solution:
    def divisorSum(self, nums: List[int], number: int) -> int:
        answer = 0

        for val in nums:
            answer += math.ceil(val / number)

        return answer

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = float('inf')

        while(low <= high):
            mid = (low + high) // 2
            res = self.divisorSum(piles, mid)
            if(res <= h):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans