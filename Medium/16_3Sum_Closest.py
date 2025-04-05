class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        closest = float('inf')

        for i, a in enumerate(nums):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue

            l = i + 1
            r = size - 1
            while(l < r):
                threeSum = a + nums[l] + nums[r]
                if(abs(threeSum - target) < abs(closest - target)):
                    closest = threeSum

                if(threeSum == target):
                    return threeSum
                elif(threeSum < target):
                    l += 1
                else:
                    r -= 1

        return closest