from functools import cmp_to_key
def compare(t1,t2):
    if(t1[0]<t2[0]):
        return -1
    if(t1[0] > t2[0]):
        return 1
    return 0

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank=[100000]*26
        for i in range(len(order)):
            rank[ord(order[i])-ord('a')]=i
        #rint(rank)
        l=[]
        for i in range(len(s)):
            l.append((rank[ord(s[i])-ord('a')],s[i]))
        l.sort(key=cmp_to_key(compare))
        s1=''
        for i in range(len(l)):
            s1+=l[i][1]
        return s1