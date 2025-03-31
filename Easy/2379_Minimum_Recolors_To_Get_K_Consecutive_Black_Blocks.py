class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blackCnt = 0

        for i in range(k):
            if(blocks[i] == "B"):
                blackCnt += 1
        
        minFlips = k - blackCnt

        for i in range(k, len(blocks)):
            if(blocks[i - k] == "B"):
                blackCnt -= 1
            
            if(blocks[i] == "B"):
                blackCnt += 1

            minFlips = min(minFlips, k - blackCnt)

        return minFlips