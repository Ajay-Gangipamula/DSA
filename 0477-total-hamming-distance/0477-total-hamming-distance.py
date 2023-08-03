class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n=len(nums)
        mask=1<<31
        ans=0
        for i in range(32):
            countofones=0
            for j in range(n):
                if(mask & nums[j]):
                    countofones+=1
            ans+=(countofones)*(n-countofones)
            mask>>=1
        return ans