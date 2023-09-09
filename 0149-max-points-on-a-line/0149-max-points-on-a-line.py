class Solution:
    def gcd(a,b):
        if a==0:
            return b
        if b==0:
            return a
        m1=max(a,b)
        m2=min(a,b)
        while(m1 % m2 == 0):
            if m1 % m2 == 0:
                return m2
            a1=m2
            m2=m1 % m2
            m1=a1
    def standardise(xdiff,ydiff):
        if(xdiff==0):
            ydiff=1
        elif(ydiff==0):
            xdiff=1
        elif((xdiff<0 and ydiff<0) or ydiff<0):
            xdiff*=-1
            ydiff*=-1
        return xdiff,ydiff
    
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)==0):
            return 0
        ans=1
        m={}
        for i in range(len(points)):
            olp=0
            maxm=0
            m={}
            for j in range(i+1,len(points)):
                if(points[i][0]==points[j][0] and points[i][1]==points[j][1]):
                    olp+=1
                else:
                    xdiff=points[j][0]-points[i][0]
                    ydiff=points[j][1]-points[i][1]
                    g = gcd(abs(xdiff),abs(ydiff))
                    xdiff,ydiff = xdiff//g,ydiff//g
                    xdiff,ydiff=Solution.standardise(xdiff,ydiff)
                    if((xdiff,ydiff) in m):
                        m[(xdiff,ydiff)]+=1
                    else:
                        m[(xdiff,ydiff)]=1
                    maxm=max(maxm,m[(xdiff,ydiff)])
            ans=max(ans,maxm+olp+1)
        return ans