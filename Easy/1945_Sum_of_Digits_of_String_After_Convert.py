class Solution:
    def getLucky(self, s: str, k: int) -> int:
        intStr=''

        for i in s:
            intStr += str(ord(i)-96)
        
        for _ in range(k):
            tot = 0           
            for i in intStr:
                tot += int(i)
            intStr = str(tot)    

        return tot

        