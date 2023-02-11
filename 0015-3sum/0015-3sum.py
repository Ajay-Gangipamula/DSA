class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l1=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while(l<r):
                totalsum=nums[i]+nums[l]+nums[r]
                if(totalsum==0):
                    if([nums[i],nums[l],nums[r]] not in l1):
                        l1.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
                elif(totalsum<0):
                    l=l+1
                elif(totalsum>0):
                    r=r-1
        return l1
            
                
            
            
        