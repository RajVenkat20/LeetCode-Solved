import math

class Solution:
    def divisorSum(self, nums: List[int], number: int) -> int:
        answer = 0

        for val in nums:
            answer += math.ceil(val / number)
        
        return answer

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = float('inf')
        low, high = 1, max(nums)

        while(low <= high):
            mid = (low + high) // 2
            res = self.divisorSum(nums, mid)
            if(res <= threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans        