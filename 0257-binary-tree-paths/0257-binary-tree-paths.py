# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def roottoleaf(root,tmp,ans):
    if(not root):
        return
    if(len(tmp)==0):
        tmp+=str(root.val)
    else:
        tmp+="->"+str(root.val)
    if((not root.left) and (not root.right)):
        ans.append(tmp)
    roottoleaf(root.left,tmp,ans)
    roottoleaf(root.right,tmp,ans)

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        tmp=""
        ans=[]
        roottoleaf(root,tmp,ans)
        return ans