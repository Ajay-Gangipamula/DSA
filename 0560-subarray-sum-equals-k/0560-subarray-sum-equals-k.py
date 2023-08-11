class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefsum=0
        d=dict()
        d[0]=1
        count=0
        for i in range(len(nums)):
            prefsum+=nums[i]
            if(prefsum-k in d):
                count+=d[prefsum-k]

            if prefsum in d:
                d[prefsum]+=1
            else:
                d[prefsum]=1
        return count