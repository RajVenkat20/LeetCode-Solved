class Solution:
    def calculate(self, s: str) -> int:
        curr = prev = res = 0
        i = 0
        
        currOp = "+"
        size = len(s)

        while(i < size):
            currChar = s[i]

            if(currChar.isdigit()):
                while(i < size and s[i].isdigit()):
                    curr = curr * 10 + int(s[i])
                    i += 1
                
                i -= 1

                if(currOp == "+"):
                    res += curr
                    prev = curr
                elif(currOp == "-"):
                    res -= curr
                    prev = -curr
                elif(currOp == "*"):
                    res -= prev
                    res += prev * curr
                    prev = curr * prev
                else:
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                
                curr = 0
            elif(currChar != " "):
                currOp = currChar
            
            i += 1
        
        return res