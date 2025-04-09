class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(position, curr, total):
            if(total == 0):
                res.append(curr[:])
            if(total <= 0):
                return

            prev = -1

            for i in range(position, len(candidates)):
                if(prev == candidates[i]):
                    continue
                curr.append(candidates[i])
                dfs(i + 1, curr, total - candidates[i])
                curr.pop()
                prev = candidates[i]

        dfs(0, [], target)

        return res