class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]

        if(n <= 2):
            return arr[n]
        for i in range(2, n):
            arr.append(arr[-1] + arr[-2] + arr[-3])
        
        return arr[-1]