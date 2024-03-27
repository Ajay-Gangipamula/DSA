# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def heightbalanced(root):
    if(not root):
        return (True,0)
    lst=heightbalanced(root.left)
    rst=heightbalanced(root.right)
    f=lst[0] and rst[0] and (abs(lst[1]-rst[1])<=1)
    return (f,1+max(lst[1],rst[1]))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return heightbalanced(root)[0]