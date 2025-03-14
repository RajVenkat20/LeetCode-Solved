class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0, 0]
        n = len(cost)

        for i in range(2, n + 1):
            next_cost = min(min_cost[i - 2] + cost[i - 2],
                            min_cost[i - 1] + cost[i - 1])

            min_cost.append(next_cost)

        return min_cost[-1]