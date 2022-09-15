from functools import cmp_to_key
def compare(k1:list,k2:list)->int:
    d1=k1[0]*k1[0]+k1[1]*k1[1]
    d2=k2[0]*k2[0]+k2[1]*k2[1]
    if(d1<d2):
        return -1
    if(d1>d2):
        return 1
    return 0

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=cmp_to_key(compare))
        l2=[]
        for i in range(k):
            l2.append(points[i])
        return l2
        #return points[:k]