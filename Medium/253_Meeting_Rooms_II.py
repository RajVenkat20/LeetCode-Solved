class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimes = []
        endTimes = []

        for start, end in intervals:
            startTimes.append(start)
            endTimes.append(end)

        startTimes.sort()
        endTimes.sort()

        i, j = 0, 0
        cnt, rooms = 0, 0

        while(i < len(intervals)):
            if(startTimes[i] < endTimes[j]):
                i += 1
                cnt += 1
            else:
                j += 1
                cnt -= 1
            rooms = max(rooms, cnt)

        return rooms