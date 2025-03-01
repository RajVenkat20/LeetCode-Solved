class Solution:
    def countFreq(self, arr, target):
        first, last = -1, -1
        size = len(arr)

        # Finding the first occurence
        low, high = 0, size -1
        while(low <= high):
            mid = (low + high) // 2
            if(arr[mid] == target):
                first = mid
                high = mid - 1
            elif(arr[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        # Finding the first occurence
        low, high = 0, size - 1
        while(low <= high):
            mid = (low + high) // 2
            if(arr[mid] == target):
                last = mid
                low = mid + 1
            elif(arr[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
                
        return 0 if first == -1 else (last - first + 1)
