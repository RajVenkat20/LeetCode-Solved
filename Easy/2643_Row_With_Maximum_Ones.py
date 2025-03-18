class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        indexes = [row.count(1) for row in mat]
        max_count = max(indexes)
        i = indexes.index(max_count)
        
        return [i, indexes[i]]