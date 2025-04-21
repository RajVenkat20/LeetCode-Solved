class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        hm = collections.defaultdict(list)
        res = []

        for i, group in enumerate(groupSizes):
            hm[group].append(i)
            if(len(hm[group]) == group):
                res.append(hm[group])
                hm[group] = []
        
        return res