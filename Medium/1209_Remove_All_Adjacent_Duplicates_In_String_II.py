class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        i = 0
        while(i < len(s)):
            if(not stack or s[i] != stack[-1][0]):
                stack.append([s[i], 1])
            else:
                stack[-1][1] += 1
                if(stack[-1][1] == k):
                    stack.pop()
            i += 1

        return ''.join(char * count for char, count in stack)