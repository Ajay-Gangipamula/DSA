def func(s,l,r,i,n,l1):
    if(l+r==2*n):
        l1.append("".join(s))
        return
    if(l==n and r<n):
        s[i]=')'
        func(s,l,r+1,i+1,n,l1)
    elif(l>r and l<n):
        s[i]='('
        func(s,l+1,r,i+1,n,l1)
        s[i]=')'
        func(s,l,r+1,i+1,n,l1)
    elif(l==r and l<n):
        s[i]='('
        func(s,l+1,r,i+1,n,l1)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l1=[]
        s=['']*(2*n)
        func(s,0,0,0,n,l1)
        return l1