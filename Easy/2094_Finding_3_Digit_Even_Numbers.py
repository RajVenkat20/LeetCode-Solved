class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hm = {}
        ans = []
         
        for i in digits:
            hm[i] = hm.get(i, 0) + 1

        for number in range(100, 999, 2):
            hm2 = {}
            x = number
            while(number > 0):
                temp = number % 10
                hm2[temp] = hm2.get(temp, 0) + 1
                number = number // 10
            
            def compare(hm1, hm2):
                for val in hm2:
                    if(hm2[val] > hm1.get(val,0)):
                        return False
                return True

            if(compare(hm, hm2)):
                ans.append(x)

        return ans