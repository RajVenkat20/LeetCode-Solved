class Solution:
    def maxDifference(self, s: str) -> int:
        hm = {}
        evenMin, oddMax = float('inf'), 0
        for char in s:
            hm[char] = hm.get(char, 0) + 1
        
        for val in hm.values():
            if(val % 2 and val > oddMax):
                oddMax = val
            elif(val % 2 == 0 and val < evenMin):
                evenMin = val

        return (oddMax - evenMin)