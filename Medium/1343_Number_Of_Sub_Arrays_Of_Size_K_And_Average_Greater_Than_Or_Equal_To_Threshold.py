class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt, total = 0, 0
        left = 0

        for i in range(k):
            total += arr[i]
        
        if(total / k >= threshold):
            cnt += 1
        
        for right in range(k, len(arr)):
            total += arr[right]
            total -= arr[left]
            left += 1

            if(total / k >= threshold):
                cnt += 1

        return cnt