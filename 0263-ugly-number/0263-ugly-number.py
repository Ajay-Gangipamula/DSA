class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        d1,d2,d3=2,3,5
        while(n % d1 ==0):
            n=n//d1
        while(n % d2 ==0):
            n=n//d2
        while(n % d3 ==0):
            n=n//d3
        return n==1