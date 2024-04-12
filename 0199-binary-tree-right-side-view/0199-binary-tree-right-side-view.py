# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class maxlvl:
    def __init__(self,val):
        self.val=val

def preorder(root,maxl,lvl,l):
    if(not root):
        return
    if(lvl>maxl.val):
        maxl.val=lvl
        l.append(root.val)
    preorder(root.right,maxl,lvl+1,l)
    preorder(root.left,maxl,lvl+1,l)


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        maxl=maxlvl(-1)
        preorder(root,maxl,0,l)
        return l