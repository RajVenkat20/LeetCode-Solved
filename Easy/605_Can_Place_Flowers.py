class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        cnt = 0
        res = [0]
        res.extend(flowerbed)
        res.append(0)

        for i in range(1, size + 1):
            if(res[i - 1] != 1 and res[i + 1] != 1 and res[i] != 1):
                res[i] = 1
                cnt += 1
                if(cnt == n):
                    return True

        return cnt >= n