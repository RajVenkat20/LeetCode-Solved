class MyHashMap:

    def __init__(self):
        self.hm = {}

    def put(self, key: int, value: int) -> None:
        self.hm[key] = value

    def get(self, key: int) -> int:
        return self.hm.get(key, -1)

    def remove(self, key: int) -> None:
        self.hm.pop(key, 0)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)