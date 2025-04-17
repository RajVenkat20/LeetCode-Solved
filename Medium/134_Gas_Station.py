class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if(sum(gas) < sum(cost)):
            return -1

        currGain = 0
        idx = 0

        for i in range(len(gas)):
            currGain += gas[i] - cost[i]

            if(currGain < 0):
                currGain = 0
                idx = i + 1

        return idx