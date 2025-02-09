class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        hm = {}
        cnt = 0

        for i in range(n):
            key = nums[i] - i
            cnt += hm.get(key, 0)
            hm[key] = hm.get(key, 0) + 1

        return (n * (n - 1)) // 2 - cnt