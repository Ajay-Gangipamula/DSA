class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        ans=0
        for i in range(len(nums)):
            if(nums[i] in d):
                continue
            else:
                ls=0
                rs=0
                if nums[i]-1 in d:
                    ls=d[nums[i]-1]
                if(nums[i]+1 in d):
                    rs=d[nums[i]+1]
                ans=max(ans,1+ls+rs)
                d[nums[i]]=1+ls+rs
                d[nums[i]+rs]=1+ls+rs
                d[nums[i]-ls]=1+ls+rs
        return ans