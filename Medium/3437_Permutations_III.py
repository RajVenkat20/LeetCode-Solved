class Solution:
    def permute(self, n: int) -> List[List[int]]:
        res = []

        def backtracking(arr, type):
            if(len(arr) == n):
                res.append(arr.copy())
                return
            
            for i in range(1, n + 1):
                if(not type):
                    arr.append(i)
                    if(i % 2):
                        backtracking(arr, "odd")
                    else:
                        backtracking(arr, "even")
                    arr.pop()
                elif(type == "even" and i % 2 and i not in arr):
                    arr.append(i)
                    backtracking(arr, "odd")
                    arr.pop()
                elif(type == "odd" and i % 2 == 0 and i not in arr):
                    arr.append(i)
                    backtracking(arr, "even")
                    arr.pop()
                    

        backtracking([], "")
        return res