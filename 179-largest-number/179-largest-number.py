from functools import cmp_to_key
def compare(t1,t2):
    if(t1!=t2):
        t1,t2=str(t1),str(t2)
        if(t1+t2 > t2+t1):
            return -1
        if(t1+t2 < t2+t1):
            return 1
        return 0
    else:
        return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=cmp_to_key(compare))
        l=''
        for i in range(len(nums)):
            l+=str(nums[i])
        if(int(l)+1==1):
            return '0'
        return l