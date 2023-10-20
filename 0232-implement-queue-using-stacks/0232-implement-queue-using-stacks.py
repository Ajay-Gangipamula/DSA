
class MyQueue:

    def __init__(self):
        self.s1=deque()
        self.s2=deque()

    def push(self, x: int) -> None:
        if(len(self.s1)==0):
            self.front=x
        self.s1.append(x)

    def pop(self) -> int:
        while(len(self.s1)!=0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        ans=self.s2[-1]
        self.s2.pop()
        if(len(self.s2)!=0):
            self.front=self.s2[-1]
        while(len(self.s2)!=0):
            self.s1.append(self.s2[-1])
            self.s2.pop()
        return ans

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.s1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()