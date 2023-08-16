class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        visited={}
        for i in range(len(nums)):
            d[nums[i]]=0
        ans=0
        for i in range(len(nums)):
            if nums[i]-1 not in d:
                if nums[i] not in visited:
                    x=nums[i]
                    count=0
                    while(x in d):
                        count+=1
                        x+=1
                    ans=max(count,ans)
                visited[nums[i]]=0
        return ans