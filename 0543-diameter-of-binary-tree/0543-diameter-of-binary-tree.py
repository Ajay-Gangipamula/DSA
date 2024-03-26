# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class mainanswer:
    def __init__(self,ans=0):
        self.ans=ans

def height(root,answer):
    if(not root):
        return 0
    h1=height(root.left,answer)
    h2=height(root.right,answer)
    answer.ans=max(answer.ans,1+h1+h2)
    return 1+max(h1,h2)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        answer=mainanswer(0)
        height(root,answer)
        return answer.ans-1