# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class answer:
    def __init__(self,ans=0):
        self.ans=ans

def getdia(root):
    if(not root):
        return (0,0)
    lst=getdia(root.left)
    rst=getdia(root.right)
    h=1+max(lst[0],rst[0])
    d=max(1+lst[0]+rst[0],lst[1],rst[1])
    return (h,d)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        return getdia(root)[1]-1