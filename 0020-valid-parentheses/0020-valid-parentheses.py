from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)==1):
            return False
        stack=deque()
        for i in range(len(s)):
            if s[i]=='{' or s[i]=='[' or s[i]=='(':
                stack.append(s[i])
            else:
                if(len(stack)==0):
                    return False
                if((s[i]=='}' and stack[-1]=='{') or (s[i]==')' and stack[-1]=='(') or (s[i]==']' and stack[-1]=='[')):
                    if(len(stack)!=0):
                        stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        else:
            return False