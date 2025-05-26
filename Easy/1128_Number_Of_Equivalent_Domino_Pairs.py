class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ans = 0

        for x, y in dominoes:
            val = 10 * x + y if x >= y else y * 10 + x
            ans += num[val]
            num[val] += 1

        return ans