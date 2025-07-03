class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minPrefix = total = 0

        for num in nums:
            total += num
            if(total < minPrefix):
                minPrefix = total

        return (abs(minPrefix) + 1) if(minPrefix <= 0) else minPrefix