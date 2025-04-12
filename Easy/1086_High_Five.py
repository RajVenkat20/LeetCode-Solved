import heapq
from collections import defaultdict
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hm = defaultdict(list)
        res = []
        for studId, val in items:
            hm[studId].append(-1 * val)
        
        for studId in hm:
            heapq.heapify(hm[studId])
            avg = 0
            for i in range(5):
                avg += (-1 * heapq.heappop(hm[studId]))

            res.append([studId, avg // 5])

        res.sort()

        return res