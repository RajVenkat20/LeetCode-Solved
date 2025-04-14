class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt, size = 0, len(arr)

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    diff1 = abs(arr[i] - arr[j])
                    diff2 = abs(arr[j] - arr[k])
                    diff3 = abs(arr[k] - arr[i])
                    if(diff1 <= a and diff2 <= b and diff3 <= c):
                        cnt +=1 

        return cnt