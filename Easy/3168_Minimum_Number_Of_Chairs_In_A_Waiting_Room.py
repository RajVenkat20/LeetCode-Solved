class Solution:
    def minimumChairs(self, s: str) -> int:
        curr, total = 0, 0

        for event in s:
            if(event == "E"):
                curr += 1
                total = max(total, curr)
            else:
                curr -= 1

        return total