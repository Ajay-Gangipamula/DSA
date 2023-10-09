from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=deque()
        nse=[0]*len(heights)
        for i in range(len(heights)):
            while(len(stk)!=0 and heights[i]<heights[stk[-1]]):
                nse[stk[-1]]=i
                stk.pop()
            stk.append(i)
        while(len(stk)!=0):
            nse[stk[-1]]=len(heights)
            stk.pop()
        pse=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while(len(stk)!=0 and heights[i]<heights[stk[-1]]):
                pse[stk[-1]]=i
                stk.pop()
            stk.append(i)
        while(len(stk)!=0):
            pse[stk[-1]]=-1
            stk.pop()
        maxarea=0
        for i in range(len(heights)):
            maxarea=max((nse[i]-pse[i]-1)*heights[i], maxarea)
        return maxarea