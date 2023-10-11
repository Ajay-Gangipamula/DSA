from collections import deque
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j]=='1'):
                    matrix[i][j]=1
                else:
                    matrix[i][j]=0

        for j in range(cols):
            for i in range(1,rows):
                if(matrix[i][j]!=0):
                    matrix[i][j]=1+matrix[i-1][j]

        maxarea=0
        for n in range(rows):
            nse=[0]*cols
            pse=[0]*cols
            stk=deque()
            stk.append(0)
            for j in range(1,cols):
                while(len(stk)!=0 and matrix[n-1][j] < matrix[n-1][stk[-1]]):
                    nse[stk[-1]]=j
                    stk.pop()
                stk.append(j)
            while(len(stk)!=0):
                nse[stk[-1]]=cols
                stk.pop()

            stk.append(cols-1)
            for j in range(cols-2,-1,-1):
                while(len(stk)!=0 and matrix[n-1][j]<matrix[n-1][stk[-1]]):
                    pse[stk[-1]]=j
                    stk.pop()
                stk.append(j)
            while(len(stk)!=0):
                pse[stk[-1]]=-1
                stk.pop()
            for j in range(cols):
                area=(nse[j]-pse[j]-1)*int(matrix[n-1][j])
                maxarea=max(maxarea,area)
        return maxarea