class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = 1
        size = len(arr)
        if(size == 1):
            return arr[0]
        for i in range(1, size):
            if(arr[i] == arr[i - 1]):
                cnt += 1
                if(cnt > size / 4):
                    return arr[i]
            else:
                cnt = 1