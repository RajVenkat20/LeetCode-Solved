class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        i = 0

        while(i < len(s)):
            curr = s[i]
            if(curr.isdigit()):
                num = ""
                while(s[i].isdigit()):
                    num = num + s[i]
                    i += 1
                i = i - 1
                stack.append(int(num))
            elif(curr == "[" or curr.isalpha()):
                stack.append(curr)
            else:
                temp = ""
                while(stack[-1] != "["):
                    temp = stack.pop() + temp
                stack.pop()
                freq = stack.pop()
                res += (temp * freq)
                stack.append(temp * freq)

            i += 1

        return "".join(stack)