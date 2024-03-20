# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxheight(root):
    if(not root):
        return 0
    lst=maxheight(root.left)
    rst=maxheight(root.right)
    return 1+max(lst,rst)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        return maxheight(root)