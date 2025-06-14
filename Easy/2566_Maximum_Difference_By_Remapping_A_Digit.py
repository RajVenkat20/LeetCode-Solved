class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        remap = "9"
        for i in range(len(num)):
            if(num[i] != '9'):
                remap = num[i]
                break
        maxNum = int(num.replace(remap, '9'))

        for i in range(len(num)):
            if(num[i] != '0'):
                remap = num[i]
                break
        minNum = int(num.replace(remap, '0'))

        return (maxNum - minNum)