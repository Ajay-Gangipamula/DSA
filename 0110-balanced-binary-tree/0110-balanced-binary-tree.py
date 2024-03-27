# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class mainanswer:
    def __init__(self,ans):
        self.ans=ans

def heightbalanced(root,answer):
    if(not root):
        return 0
    h1=heightbalanced(root.left,answer)
    h2=heightbalanced(root.right,answer)
    if(abs(h1-h2)>1):
        answer.ans=False
    return 1+max(h1,h2)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer=mainanswer(True)
        heightbalanced(root,answer)
        return answer.ans