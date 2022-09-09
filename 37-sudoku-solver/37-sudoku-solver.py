def mat_num(i,j):
    if(i>=0 and i<=2):
        if(j>=0 and j<=2):
            return 0
        elif(j>=3 and j<=5):
            return 1
        else:
            return 2
    elif(i>=3 and i<=5):
        if(j>=0 and j<=2):
            return 3
        elif(j>=3 and j<=5):
            return 4
        else:
            return 5
    else:
        if(j>=0 and j<=2):
            return 6
        elif(j>=3 and j<=5):
            return 7
        else:
            return 8


def func(board,i,j,ansfound,rf,cf,matf,ans):
    #print(board)
    if(ansfound==True):
        return
    if(i==9):
        for i in range(9):
            for j in range(9):
                ans[i][j]=board[i][j]
        ansfound=True
        #print(board)
        return
    if(board[i][j]!='.'):
        if(j>=8):
            func(board,i+1,0,ansfound,rf,cf,matf,ans)
        else:
            func(board,i,j+1,ansfound,rf,cf,matf,ans)
        return
    matnum=mat_num(i,j)
    for c in range(1,10):
        if(rf[i][c-1]==0 and cf[j][c-1]==0 and matf[matnum][c-1]==0):
            board[i][j]=str(c)
            rf[i][c-1]=1
            cf[j][c-1]=1
            matf[matnum][c-1]=1
            if(j==8):
                func(board,i+1,0,ansfound,rf,cf,matf,ans)
            else:
                func(board,i,j+1,ansfound,rf,cf,matf,ans)
            board[i][j]='.'
            rf[i][c-1]=0
            cf[j][c-1]=0
            matf[matnum][c-1]=0

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        ansfound=False
        rf=[]
        for i in range(9):
            l=[0]*9
            for j in range(9):
                if(board[i][j]!='.'):
                    l[int(board[i][j])-1]+=1
            rf.append(l)
        cf=[]
        for j in range(9):
            l=[0]*9
            for i in range(9):
                if(board[i][j]!='.'):
                    l[int(board[i][j])-1]+=1
            cf.append(l)
        matf=[]
        for i in range(0,9,3):
            for j in range(0,9,3):
                l=[0]*9
                for i1 in range(i,i+3):
                    for j1 in range(j,j+3):
                        if(board[i1][j1]!='.'):
                            l[int(board[i1][j1])-1]+=1
                matf.append(l)
        ans=[]
        for i in range(9):
            ans.append([0]*9)
        func(board,0,0,ansfound,rf,cf,matf,ans)
        for i in range(9):
            for j in range(9):
                board[i][j]=ans[i][j]
        """
        Do not return anything, modify board in-place instead.
        """
        