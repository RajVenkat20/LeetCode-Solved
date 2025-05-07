class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openP = closeP = 0
        stack = []
        res = []
        
        def backtrack(op, cl):
            if(op == cl == n):
                res.append("".join(stack))
                return
            if(op < n):
                stack.append("(")
                backtrack(op + 1, cl)
                stack.pop()
            if(cl < op):
                stack.append(")")
                backtrack(op, cl + 1)
                stack.pop() 

        backtrack(0, 0)
        return res