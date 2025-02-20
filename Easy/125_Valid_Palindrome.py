class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []

        for i in s:
            if(i.isalnum()):
                arr.append(i)

        l = 0
        r = len(arr) - 1

        while(l <= r):
            if(arr[l] == arr[r]):
                l += 1
                r -= 1
            else:
                return False

        return True