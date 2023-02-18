class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        i=0
        while(i<n):
            if(nums[i]>=0):
                break
            i+=1
        j=i-1
        while(j>=0 and i<n):
            if(nums[i]*nums[i] < nums[j]*nums[j]):
                ans.append(nums[i]*nums[i])
                i+=1
            else:
                ans.append(nums[j]*nums[j])
                j=j-1
        while(j>=0):
            ans.append(nums[j]*nums[j])
            j=j-1
        while(i<n):
            ans.append(nums[i]*nums[i])
            i+=1
        return ans