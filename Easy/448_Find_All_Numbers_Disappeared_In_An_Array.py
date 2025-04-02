class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        temp = set(nums)
        for num in range(1, len(nums) + 1):
            if(num not in temp):
                res.append(num)

        return res