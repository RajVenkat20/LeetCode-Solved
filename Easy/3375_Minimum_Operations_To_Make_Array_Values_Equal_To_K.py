class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = set()

        for num in nums:
            if(num < k):
                return -1
            elif(num > k):
                ans.add(num)

        return len(ans)