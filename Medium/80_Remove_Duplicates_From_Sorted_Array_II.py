class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        size = len(nums)
        while(right < size):
            cnt = 1
            while(right + 1 < size and nums[right] == nums[right + 1]):
                cnt += 1
                right += 1

            for i in range(min(2, cnt)):
                nums[left] = nums[right]
                left += 1

            right += 1

        return left