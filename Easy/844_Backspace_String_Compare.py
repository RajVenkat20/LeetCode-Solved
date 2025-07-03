class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []

        for char in s:
            if(char.isalpha()):
                stack1.append(char)
            else:
                if(stack1):
                    stack1.pop()

        for char in t:
            if(char.isalpha()):
                stack2.append(char)
            else:
                if(stack2):
                    stack2.pop()

        return stack1 == stack2