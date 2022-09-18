from functools import cmp_to_key
def compare(t1:tuple,t2:tuple)->int:
    if(t1[0]!=t2[0]):
        if(t1[1] < t2[1]):
            return -1
        if(t1[1] > t2[1]):
            return 1
        if(t1[1]==t2[1]):
            if(t1[0] < t2[0]):
                return -1
            if(t1[0] > t2[0]):
                return 1
            return 0
    return 0

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arrcount=[100000000]*1001
        for i in range(len(arr2)):
            arrcount[arr2[i]-1]=i+1
        l=[]
        for i in range(len(arr1)):
            l.append((arr1[i],arrcount[arr1[i]-1]))
        l.sort(key=cmp_to_key(compare))
        l1=[]
        for i in l:
            l1.append(i[0])
        return l1