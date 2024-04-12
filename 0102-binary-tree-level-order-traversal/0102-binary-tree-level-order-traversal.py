# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=deque()
        if(root):
            que.append(root)
        l1=[]
        while(len(que)!=0):
            l=[]
            length=len(que)
            while(length > 0):
                r=que[0]
                que.popleft()
                l.append(r.val)
                if(r.left):
                    que.append(r.left)
                if(r.right):
                    que.append(r.right)
                length=length-1
            l1.append(l)
        return l1