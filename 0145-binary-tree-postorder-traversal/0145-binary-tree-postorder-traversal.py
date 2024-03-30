# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorder(root,l):
    if(not root):
        return
    postorder(root.left,l)
    postorder(root.right,l)
    l.append(root.val)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        postorder(root,l)
        return l