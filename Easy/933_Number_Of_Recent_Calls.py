class RecentCounter:
    def __init__(self):
        self.window = deque()

    def ping(self, t: int) -> int:
        self.window.append(t)
        
        while(self.window[0] < t - 3000):
            self.window.popleft()

        return len(self.window)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)