# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorder(root):
    stk=deque()
    stk.append((root,0))
    l=[]
    while(len(stk)!=0):
        r=stk[-1]
        stk.pop()
        if(r[1]==1):
            l.append(r[0].val)
        else:
            if(r[0]):
                stk.append((r[0],1))
                if(r[0].right):
                    stk.append((r[0].right,0))
                if(r[0].left):
                    stk.append((r[0].left,0))
    return l



class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=postorder(root)
        return l