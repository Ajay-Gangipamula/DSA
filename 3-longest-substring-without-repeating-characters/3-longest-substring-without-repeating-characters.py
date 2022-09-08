class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        l=list(s)
        if(len(s)==0):
            return 0
        elif(len(s)==1):
            return 1
        
        for i in range(len(s)-1):
            d=dict()
            j=i
            csum=0
            while(j<len(s)):
                if(l[j] not in d):
                    d[l[j]]=1
                    #print(d)
                    csum=csum+1
                    maxi=max(csum,maxi)
                else:
                    j=len(s)
                j=j+1
        return maxi
            
                
                