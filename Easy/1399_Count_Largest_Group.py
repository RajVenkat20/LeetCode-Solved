class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        hm = collections.defaultdict(int)

        def digitSum(n):
            tot = 0
            while(n > 0):
                tot += (n % 10)
                n = n // 10
            return tot

        for i in range(1, n + 1):
            hm[digitSum(i)] += 1

        maxSize = max(hm.values())
        cnt = 0

        for v in hm.values():
            if(v == maxSize):
                cnt += 1

        return cnt