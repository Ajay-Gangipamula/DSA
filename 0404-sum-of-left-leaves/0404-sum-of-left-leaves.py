# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def countLeaves(root,d):
    # Code here
    if(not root):
        return 0
    if((not root.left) and (not root.right)):
        if d==1:
            return root.val
        else:
            return 0
    return countLeaves(root.left,1)+countLeaves(root.right,0)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        return countLeaves(root.left,1)+countLeaves(root.right,0)