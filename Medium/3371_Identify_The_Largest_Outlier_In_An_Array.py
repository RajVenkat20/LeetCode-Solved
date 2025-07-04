class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)

        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        outlier = float('-inf')

        for num in hm.keys():
            potentialOutlier = total - (2 * num) 

            if(potentialOutlier in hm):
                if(potentialOutlier != num or hm[num] > 1):
                    outlier = max(outlier, potentialOutlier)
        
        return outlier