class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = {}

        for num in arr:
            hm[num] = hm.get(num, 0) + 1

        largest = -1
        for key in hm:
            if(hm[key] == key):
                largest = max(largest, key)

        return largest