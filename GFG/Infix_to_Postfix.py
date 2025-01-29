#User function Template for python3


class Solution:
    def precedence(self, char):
        if(char == '^'):
            return 3
        elif(char == '/' or char == '*'):
            return 2
        elif(char == '+' or char == '-'):
            return 1
        else:
            return -1
    
    def InfixtoPostfix(self, s):
        res = ""
        stack = []
        
        for char in s:
            if(char.isalnum()):
                res += char
            elif(char == '('):
                stack.append(char)
            elif(char == ')'):
                while(stack[-1] != '('):
                    res += stack.pop()
                stack.pop()
            else:
                while(stack and (self.precedence(char) < self.precedence(stack[-1]) or self.precedence(char) == self.precedence(stack[-1]))):
                    res += stack.pop()
                    
                stack.append(char)
                
        while(stack):
            res += stack.pop()

        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        exp = str(input())
        ob = Solution()
        print(ob.InfixtoPostfix(exp))
        print("~")

# } Driver Code Ends