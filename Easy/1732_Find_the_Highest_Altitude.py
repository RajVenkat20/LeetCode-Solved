class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        size = len(gain)
        highest = 0
        temp = 0
        
        for i in range(size):
            if(temp + gain[i] > highest):
                highest = temp + gain[i]
            temp = temp + gain[i]

        return highest