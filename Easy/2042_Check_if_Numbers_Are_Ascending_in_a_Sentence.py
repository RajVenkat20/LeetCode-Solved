class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        first, second = -1, -1
        for var in s:
            if(var[0] in '0123456789'):
                first = int(var)
                if(first <= second):
                    return False
                second = first                

        return True