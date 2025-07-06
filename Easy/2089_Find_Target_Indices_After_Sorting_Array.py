class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt, smaller = 0, 0
        for num in nums:
            if(num == target):
                cnt += 1
            elif(num < target):
                smaller += 1

        res = []
        for i in range(smaller, smaller + cnt):
            res.append(i)

        return res