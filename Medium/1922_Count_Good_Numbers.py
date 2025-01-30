class Solution:
    def power(self, x, n, mod=10**9 + 7):
        if(n == 0):
            return 1
        if(n % 2 == 0):
            return self.power((x * x) % mod, n//2)
        else:
            return (x * self.power((x * x) % mod, n//2)) % mod


    def countGoodNumbers(self, n: int) -> int:
        if(n % 2 == 0):
            even = n // 2
            odd = n // 2
        else:
            even = n // 2 + 1
            odd = n // 2 
        
        return (self.power(5, even) * self.power(4, odd)) % (10**9 + 7)