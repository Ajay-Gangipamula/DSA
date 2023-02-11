def func(nums,i,count1):
    if(i==len(nums)):
        count1[0]+=1
        return
    for j in range(i,len(nums)):
        if(nums[j]%(i+1)==0 or (i+1)%nums[j]==0):
            nums[i],nums[j]=nums[j],nums[i]
            func(nums,i+1,count1)
            nums[i],nums[j]=nums[j],nums[i]


class Solution:
    def countArrangement(self, n: int) -> int:
        nums=[]
        for x in range(1,n+1):
            nums.append(x)
        count1=[0]
        func(nums,0,count1)
        return count1[0]