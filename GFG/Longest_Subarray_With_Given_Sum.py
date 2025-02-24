# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        mp = {}
        res = 0
        prefix_sum = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            # If prefix sum is same as k, we have a prefix subarray from 0 to i
            if prefix_sum == k:
                res = i + 1

            # Check if prefix_sum - k exists in the map
            if prefix_sum - k in mp:
                res = max(res, i - mp[prefix_sum - k])

            # Insert prefix_sum in the map if not already present
            if prefix_sum not in mp:
                mp[prefix_sum] = i

        return res