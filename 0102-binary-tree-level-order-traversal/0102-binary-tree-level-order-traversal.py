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
            que.append((root,0))
        curr_lvl=0
        l=[]
        l1=[]
        while(len(que)!=0):
            p=que[0]
            que.popleft()
            if(p[1] > curr_lvl):
                curr_lvl=p[1]
                l1.append(l)
                l=[]
            l.append(p[0].val)
            if(p[0].left):
                que.append((p[0].left,p[1]+1))
            if(p[0].right):
                que.append((p[0].right,p[1]+1))
        if(len(l)>0):
            l1.append(l)
        return l1