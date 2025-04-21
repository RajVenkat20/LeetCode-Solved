class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        total = 0
        hm = collections.defaultdict(int)
        for ans in answers:
            hm[ans] += 1

        for k, v in hm.items():
            total += math.ceil(float(v) / (k + 1)) * (k + 1)

        return int(total)