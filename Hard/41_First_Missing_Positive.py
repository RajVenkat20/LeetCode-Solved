class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        size = len(A)
        for i in range(size):
            if(A[i] < 0):
                A[i] = 0

        for i in range(size):
            val = abs(A[i])
            if(1 <= val <= size):
                if(A[val - 1] > 0):
                    A[val - 1] *= -1
                elif(A[val - 1] == 0):
                    A[val - 1] = -1 * (size + 1)

        for i in range(1, size + 1):
            if(A[i - 1] >= 0):
                return i

        return len(A) + 1