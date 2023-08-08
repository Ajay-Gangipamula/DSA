class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x1=0
        for i in range(len(nums)):
            x1=(x1^nums[i])
        b=1
        while(not (b&x1)):
            b=b<<1
        n1=0
        for i in range(len(nums)):
            if(b & nums[i]):
                n1=(n1^nums[i])
        n2=(n1^x1)
        return [n1,n2]