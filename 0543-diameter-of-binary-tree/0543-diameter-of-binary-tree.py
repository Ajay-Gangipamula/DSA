# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if(not root):
        return 0
    return 1+max(height(root.left),height(root.right))


def getdia(root):
    if(not root):
        return 0
    return max(1+height(root.left)+height(root.right),getdia(root.left),getdia(root.right))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        return getdia(root)-1