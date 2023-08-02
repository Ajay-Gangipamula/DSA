class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        shift=(1<<31)
        for i in range(len(nums)):
            nums[i]+=shift
        ans=0
        mask= (1<<31)
        for i in range(32):
            cnt=0
            for j in range(len(nums)):
                if(nums[j] & mask):
                    cnt+=1
            if(cnt%3!=0):
                ans+=mask
            mask=(mask>>1)
        return ans-shift