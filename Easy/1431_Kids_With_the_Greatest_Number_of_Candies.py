class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        size = len(candies)
        res = [False] * size
        greatest = -1

        for i in candies:
            if(greatest < i):
                greatest = i
        
        for i in range(size):
            if(candies[i] + extraCandies >= greatest):
                res[i] = True

        return res