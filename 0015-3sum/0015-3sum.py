class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        n=len(nums)
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            a=-1*nums[i]
            j=i+1
            k=n-1
            while(j<k):
                if(nums[j]+nums[k]==a):
                    l.append((-a,nums[j],nums[k]))
                    if(nums[j]==nums[k]):
                        break
                    else:
                        x=nums[j]
                        y=nums[k]
                        while(nums[j]==x):
                            j+=1
                        while(nums[k]==y):
                            k-=1
                elif(nums[j]+nums[k]<a):
                    j+=1
                else:
                    k-=1
        return l