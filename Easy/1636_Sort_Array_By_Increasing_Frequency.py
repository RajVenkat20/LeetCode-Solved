class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)
        return sorted(nums, key = lambda x: (freq[x], -x))