class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.hm
        if(res):
            self.hm[val] = len(self.numList)
            self.numList.append(val)

        return res

    def remove(self, val: int) -> bool:
        res = val in self.hm
        if(res):
            idx = self.hm[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.hm[lastVal] = idx
            del self.hm[val]

        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()