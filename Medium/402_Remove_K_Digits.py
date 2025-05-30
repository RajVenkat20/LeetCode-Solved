class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if(len(num) <= k):
            return "0"
        for c in num:
            while(k > 0 and stack and stack[-1] > c):
                k -= 1
                stack.pop()
            stack.append(c)

        stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip("0")
       
        return res if res else "0"