class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask=1 << 31
        ans=0
        while(mask):
            if((mask & left) == (mask & right)):
                if(mask & left):
                    ans+=mask
                mask=(mask>>1)
            else:
                break
        return ans