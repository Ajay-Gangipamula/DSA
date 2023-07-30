class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr=[0]*n
        arr[0]=1
        p2,p3,p5=0,0,0
        for i in range(1,n):
            mini=min(arr[p2]*2,arr[p3]*3,arr[p5]*5)
            arr[i]=mini
            if(mini==arr[p2]*2):
                p2+=1
            if(mini==arr[p3]*3):
                p3+=1
            if(mini==arr[p5]*5):
                p5+=1
        return arr[n-1]