class Solution:
    def canShip(self, weights, n, capacity) -> int:
        cnt, load = 1, 0

        for i in range(len(weights)):
            if(load + weights[i] > capacity):
                cnt += 1
                load = weights[i]
            else:
                load += weights[i]

        return cnt

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans, n = -1, len(weights)

        while(low <= high):
            mid = (low + high) // 2
            count = self.canShip(weights, n, mid)
            if(count <= days):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
