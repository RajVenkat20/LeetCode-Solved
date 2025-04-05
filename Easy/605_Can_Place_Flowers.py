class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        res = [0] + flowerbed + [0]

        for i in range(1, size + 1):
            if(res[i - 1] == 0 and res[i + 1] == 0 and res[i] == 0):
                res[i] = 1
                n -= 1

        return n <= 0