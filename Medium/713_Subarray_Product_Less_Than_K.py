class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        left = 0
        prod = 1

        for right in range(len(nums)):
            prod *= nums[right]
            while(left <= right and prod >= k):
                prod = prod // nums[left]
                left += 1

            cnt += (right - left + 1)

        return cnt