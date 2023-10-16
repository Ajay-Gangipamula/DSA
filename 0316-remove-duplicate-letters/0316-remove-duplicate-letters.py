from collections import deque
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        stk=deque()
        freq=[0]*26
        present=[0]*26
        for i in range(n):
            freq[ord(s[i])-97]+=1
        stk.append(s[0])
        freq[ord(s[0])-97]-=1
        present[ord(s[0])-97]=1

        for i in range(1,n):
            freq[ord(s[i])-97]-=1
            if(present[ord(s[i])-97]):
                continue
            while(len(stk)!=0 and s[i]<stk[-1] and freq[ord(stk[-1])-97]>0):
                present[ord(stk[-1])-97]=0
                stk.pop()
            stk.append(s[i])
            present[ord(s[i])-97]=1

        stk1=deque()
        while(len(stk)!=0):
            stk1.append(stk[-1])
            stk.pop()
        s1=''
        while(len(stk1)!=0):
            s1+=stk1[-1]
            stk1.pop()
        return s1