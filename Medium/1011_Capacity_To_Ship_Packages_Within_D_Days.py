class Solution:
    def canShip(self, weights: List[int], capacity: int, days: int) -> bool:
        cnt, flag = 1, False
        size = capacity
        i = 0

        while(i < len(weights)):
            if(weights[i] <= size):
                size -= weights[i]
                i += 1
            else:
                cnt += 1
                size = capacity

        return cnt <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans = -1

        while(low <= high):
            mid = (low + high) // 2
            if(self.canShip(weights, mid, days)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
