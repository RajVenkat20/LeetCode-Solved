class Solution:
    def maxPower(self, s: str) -> int:
        power, res = 1, 1

        for i in range(len(s) - 1):
            if(s[i] == s[i + 1]):
                power += 1
                res = max(power, res)
            else:
                power = 1

        return res