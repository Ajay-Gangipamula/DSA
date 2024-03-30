# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root,l):
    if(not root):
        return
    inorder(root.left,l)
    l.append(root.val)
    inorder(root.right,l)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        inorder(root,l)
        return l