def issafe(r,c,n,board):
    for i in range(r):
        if(board[i][c]!='.'):
            return False
    i=r-1
    j=c-1
    while(i>=0 and j>=0):
        if(board[i][j]!='.'):
            return False
        i=i-1
        j=j-1
    i=r-1
    j=c+1
    while(i>=0 and j<n):
        if(board[i][j]!='.'):
            return False
        i=i-1
        j=j+1
    return True


def func(board,r,n,l):
    if(r==n):
        #print(board)
        l1=[]
        for i in board:
            l1.append(''.join(i))
        l.append(l1)
        return
    for c in range(n):
        if(issafe(r,c,n,board)):
            board[r][c]='Q'
            func(board,r+1,n,l)
            board[r][c]='.'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[]
        for i in range(n):
            board.append(['.']*n)
        l=[]
        func(board,0,n,l)
        return l
