class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for element in derived:
            ans = ans ^ element

        return ans == 0