# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getmaxpath(root):
    if(not root):
        return (-1001,0)
    lst=getmaxpath(root.left)
    rst=getmaxpath(root.right)
    max_sum_path = max(root.val + max(0,lst[1])+max(0,rst[1]) , lst[0], rst[0])
    max_uni_path = root.val + max(0,lst[1],rst[1])
    return (max_sum_path,max_uni_path)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return (0,0)
        a=getmaxpath(root)
        return max(a)