class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()
        usedCap = 0

        for time, passengers in timestamp:
            usedCap += passengers
            if(usedCap > capacity):
                return False

        return True