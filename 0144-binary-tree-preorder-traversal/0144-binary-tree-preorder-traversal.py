# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


def preorder(root):
    stk=deque()
    stk.append(root)
    l=[]
    while(len(stk)!=0):
        r=stk[-1]
        stk.pop()
        if(r):
            l.append(r.val)
            if(r.right):
                stk.append(r.right)
            if(r.left):
                stk.append(r.left)
    return l

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=preorder(root)
        return l