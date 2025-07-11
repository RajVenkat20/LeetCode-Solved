class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        size = len(changed)
        if(size % 2):
            return []

        res = []
        hm = collections.defaultdict(int)

        changed.sort()

        for num in changed:
            hm[num] += 1

        for num in changed:
            if(hm[num] > 0):
                hm[num] -= 1
                double = 2 * num
                if(double in hm and hm[double] > 0):
                    hm[double] -= 1
                    res.append(num)
                else:
                    return []

        return res