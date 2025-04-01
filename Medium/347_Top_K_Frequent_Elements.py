class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for n, c in hm.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res        