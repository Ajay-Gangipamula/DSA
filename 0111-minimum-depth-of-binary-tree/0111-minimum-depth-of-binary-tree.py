# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minheight(root):
    if(not root):
        return 1000000
    if((not root.right) and (not root.left)):
        return 1
    lst=minheight(root.left)
    rst=minheight(root.right)
    return 1+min(lst,rst)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        return minheight(root)