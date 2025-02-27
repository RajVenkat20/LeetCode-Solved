class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        N = len(digits)
        ans = set()
        
        for i in range(N):
            if(digits[i] != 0):
                for j in range(N):
                    if(i != j):
                        for k in range(N):
                            if(i != k and j != k and digits[k] % 2 == 0):
                                ans.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return sorted(list(ans))