class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        countofzeros=0
        end=0
        countofones=0
        maxi1=0
        tempcount=0
        if k==0:
            for i in range(len(nums)):
                if(nums[i]==1):
                    tempcount+=1
                else:
                    tempcount=0
                maxi1=max(maxi1,tempcount)
            return maxi1

        for i in range(len(nums)):
            if(nums[i]==0):
                countofzeros+=1
                if(countofzeros==k):
                    end=i
                    break
            else:
                countofones+=1
            if(i==len(nums)-1):
                end=i
                break

        start=0
        maxm=end-start+1
        while(end<len(nums)):
            while(countofzeros > k):
                if(nums[start]==0):
                    countofzeros-=1
                start+=1

            if(end-start+1 > maxm):
                maxm=end-start+1

            end+=1
            if(end<len(nums)):
                if(nums[end]==0):
                    countofzeros+=1
            
        return maxm