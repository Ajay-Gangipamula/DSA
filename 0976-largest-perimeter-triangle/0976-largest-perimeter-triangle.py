def func(a,b,c):
    if(b+c>a):
        return True
    return False
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        #print(nums)
        for i in range(n-1,1,-1):
            #print(nums[i],nums[i-1],nums[i-2],'aaa')
            if(func(nums[i],nums[i-1],nums[i-2])):
                #print(nums[i],nums[i-1],nums[i-2],'bbb')
                return nums[i]+nums[i-1]+nums[i-2]
        return 0