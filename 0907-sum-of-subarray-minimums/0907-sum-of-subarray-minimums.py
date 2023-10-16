from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        m=10**9 +7
        n=len(arr)
        nse=[0]*n
        psoe=[0]*n
        stk=deque()
        stk.append(0)
        for i in range(1,n):
            while(len(stk)!=0 and arr[i]<arr[stk[-1]]):
                nse[stk[-1]]=i
                stk.pop()
            stk.append(i)
        while(len(stk)!=0):
            nse[stk[-1]]=n
            stk.pop()

        stk.append(n-1)
        for i in range(n-2,-1,-1):
            while(len(stk)!=0 and arr[i]<=arr[stk[-1]]):
                psoe[stk[-1]]=i
                stk.pop()
            stk.append(i)
        while(len(stk)!=0):
            psoe[stk[-1]]=-1
            stk.pop()

        sum1=0
        for i in range(n):
            x1=(i-psoe[i])
            x2=nse[i]-i
            x= (((x1%m * x2%m)%m) * (arr[i]%m))%m
            sum1=(sum1%m + x%m)%m
        return sum1