from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, pairs, n = 0, 0, len(nums)
        hm = defaultdict(int)
        left = 0

        for right in range(n):
            pairs += hm[nums[right]]
            hm[nums[right]] += 1

            while(pairs >= k):
                count += (n - right)
                hm[nums[left]] -= 1
                pairs -= hm[nums[left]]
                left += 1
        
        return count