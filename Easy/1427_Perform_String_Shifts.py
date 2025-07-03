class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        overall = [0, 0]
        size = len(s)

        for direc, amt in shift:
            overall[direc] += amt

        left, right = overall

        if(left > right):
            left = (left - right) % size
            s = s[left:] + s[:left]
        else:
            right = (right - left) % size
            s = s[-right:] + s[:-right]

        return s