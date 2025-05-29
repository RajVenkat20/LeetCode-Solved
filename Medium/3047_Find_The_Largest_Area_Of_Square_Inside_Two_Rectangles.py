class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                lastStartingX = max(bottomLeft[i][0], bottomLeft[j][0])
                firstEndingX = min(topRight[i][0], topRight[j][0])

                lastStartingY = max(bottomLeft[i][1], bottomLeft[j][1])
                firstEndingY = min(topRight[i][1], topRight[j][1])

                if(lastStartingX < firstEndingX and lastStartingY < firstEndingY):
                    l, b = (firstEndingX - lastStartingX), (firstEndingY - lastStartingY)
                    side = min(l, b)
                    res = max(res, side * side)

        return res