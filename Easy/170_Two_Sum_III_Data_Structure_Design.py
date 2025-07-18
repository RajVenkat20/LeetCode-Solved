class TwoSum:

    def __init__(self):
        self.numCounts = {}

    def add(self, number: int) -> None:
        self.numCounts[number] = self.numCounts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for a in self.numCounts.keys():
            b = value - a
            if(a != b):
                if(b in self.numCounts):
                    return True
            elif(self.numCounts[a] > 1):
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)