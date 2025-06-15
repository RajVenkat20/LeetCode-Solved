class Solution:
    def maxDiff(self, num: int) -> int:
        maxNum = minNum = str(num)

        for digit in maxNum:
            if(digit != "9"):
                maxNum = maxNum.replace(digit, "9")
                break

        for idx, digit in enumerate(minNum):
            if(idx == 0):
                if(digit != "1"):
                    minNum = minNum.replace(digit, "1")
                    break
            else:
                if(digit != "0" and minNum[0] != digit):
                    minNum = minNum.replace(digit, "0")
                    break

        return int(maxNum) - int(minNum)