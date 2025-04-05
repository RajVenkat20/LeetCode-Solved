class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        size = len(numbers)
        j = size - 1
        if(size > 0):
            while(i<j):
                if(numbers[i] + numbers[j] == target):
                    return [i+1,j+1]
                elif( numbers[i] + numbers[j] < target ):
                    i = i + 1
                else:
                    j = j - 1