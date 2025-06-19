class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lowerBound = float('-inf')

        for num in preorder:
            while(stack and stack[-1] < num):
                lowerBound = stack.pop()

            if(num < lowerBound):
                return False

            stack.append(num)

        return True