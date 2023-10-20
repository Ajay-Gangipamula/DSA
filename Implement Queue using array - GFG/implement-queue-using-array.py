#User function Template for python3

class MyQueue:
    def __init__(self):
        self.queue=[0]*100000
        self.front=0
        self.back=-1
    #Function to push an element x in a queue.
    def push(self, x):
        self.back+=1
        self.queue[self.back]=x
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if(self.front>self.back):
            return -1
        else:
            x1=self.queue[self.front]
            self.front+=1
        return x1
         # add code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends