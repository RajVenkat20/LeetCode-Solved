class Solution:
    def merge(self, arr : List[int], low : int, mid : int, high : int) -> int:
        temp = []
        left = low
        right = mid + 1
        cnt = 0

        while(left <= mid and right <= high):
            if(arr[left] > 2 * arr[right]):
                cnt += (mid - left + 1)
                right += 1
            else:
                left += 1
        
        left = low
        right = mid + 1

        while(left <= mid and right <= high):
            if(arr[left] <= arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while(left <= mid):
            temp.append(arr[left])
            left += 1
        
        while(right <= high):
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return cnt

    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        cnt = 0
        if(low >= high):
            return cnt
        mid = (low + high) // 2

        cnt += self.mergeSort(nums, low, mid)
        cnt += self.mergeSort(nums, mid + 1, high)
        cnt += self.merge(nums, low, mid, high)

        return cnt       

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)
        