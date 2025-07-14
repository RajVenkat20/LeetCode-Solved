class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        longest = 0
        hashSet = set(arr)

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, curr = arr[i], arr[j]
                nxt = prev + curr
                size = 2
                
                while(nxt in hashSet):
                    size += 1
                    prev, curr = curr, nxt
                    nxt = prev + curr
                    longest = max(longest, size)
                
        return longest