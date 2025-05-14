class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if(not self.store[key]):
            return ans
        
        l, r = 0, len(self.store[key]) - 1
        
        while(l <= r):
            mid = (l + r) // 2
            val, time = self.store[key][mid]
            if(time > timestamp):
                r = mid - 1
            elif(time <= timestamp):
                ans = val
                l = mid + 1

        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)