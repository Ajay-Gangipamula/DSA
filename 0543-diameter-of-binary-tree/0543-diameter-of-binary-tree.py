# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def height(root,d):
    if(not root):
        return 0
    h1=height(root.left,d)
    h2=height(root.right,d)
    d[root]=1+max(h1,h2)
    return 1+max(h1,h2)


def getdia(root,d):
    if(not root):
        return 0
    return max(1+d[root.left]+d[root.right],getdia(root.left,d),getdia(root.right,d))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d={None: 0}
        height(root,d)
        if(not root):
            return 0
        return getdia(root,d)-1