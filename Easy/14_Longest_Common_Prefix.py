class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        a = strs[0]
        b = strs[-1]
        size = min(len(a), len(b))
        for i in range(size):
            if(a[i] != b[i]):
                return result
            result += a[i]

        return result