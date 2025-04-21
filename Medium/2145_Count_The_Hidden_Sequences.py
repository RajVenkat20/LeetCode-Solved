class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        curr = 0
        mini = maxi = 0
        for i in range(len(differences)):
            curr += differences[i]
            mini = min(mini, curr)
            maxi = max(maxi, curr)
            if(maxi - mini > upper - lower):
                return 0

        return (upper - maxi) - (lower - mini) + 1