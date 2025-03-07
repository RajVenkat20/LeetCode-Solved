class Solution:
    def bouquetCheck(self, nums: List[int], day: int, m: int, k: int) -> bool:
        cnt = 0
        numBouquet = 0

        for i in range(len(nums)):
            if(nums[i] <= day):
                cnt += 1
            else:
                numBouquet += (cnt // k)
                cnt = 0

        numBouquet += (cnt // k)
        if(numBouquet >= m):
            return True
        else:
            return False
    

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        if(m * k > n):
            return -1 

        while(low <= high):
            mid = (low + high) // 2
            result = self.bouquetCheck(bloomDay, mid, m, k)

            if(result):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
