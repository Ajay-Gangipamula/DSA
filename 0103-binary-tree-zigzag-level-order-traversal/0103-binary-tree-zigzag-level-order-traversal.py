# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=deque()
        if(root):
            que.append(root)
        l1=[]
        level=0
        stk=deque()
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
            if(level%2 == 0):
                l1.append(l)
            else:
                l1.append(l[::-1])
            level+=1
        return l1