class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt=[0]*256
        freqs=[0]*256
        distchars=0
        count=0
        start=0
        end=0
        for i in range(len(t)):
            freqt[ord(t[i])]+=1
            if(freqt[ord(t[i])]==1):
                distchars+=1

        for i in range(len(s)):
            freqs[ord(s[i])]+=1
            if(freqs[ord(s[i])]==freqt[ord(s[i])]):
                count+=1
            if(count==distchars):
                end=i
                break
        if(count<distchars):
            return ""
        minm=end-start+1
        anss=start
        anse=end
        while(end<len(s)):
            while(freqs[ord(s[start])] > freqt[ord(s[start])]):
                freqs[ord(s[start])]-=1
                start+=1
            if(end-start+1 < minm):
                anss=start
                anse=end
                minm=end-start+1
            end+=1
            if(end<len(s)):
                freqs[ord(s[end])]+=1
        return s[anss:anse+1]