class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        total = 0

        for num in nums:
            if(hm[num] > 0):
                hm[num] -= 1
                total += hm[num]

        return total