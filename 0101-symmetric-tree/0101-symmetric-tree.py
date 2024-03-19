# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def ismirror(r1,r2):
    if((not r1) and (not r2)):
        return True
    if((not r1) or (not r2)):
        return False
    return r1.val==r2.val and ismirror(r1.left,r2.right) and ismirror(r1.right,r2.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return ismirror(root.left,root.right)