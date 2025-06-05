class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = []
        temp.extend(nums[-k:])
        temp.extend(nums[:-k])
        
        n = len(nums)

        for i in range(n):
            nums[i] = temp[i]

        