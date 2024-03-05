# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(q):
    curr=q
    prev=None
    while(curr):
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

def please_print(tempora):
    while(tempora):
        print(tempora.val,"->",end="")
        tempora=tempora.next
    print()

def recurse(p,k1,k):
    if(k1<k):
        return p
    temp1=p
    tail=p
    '''while(temp1):
        
        print(temp1.val,end=" ")
        temp1=temp1.next
    print()'''
    l=1
    while(tail and l<k):
        l+=1
        tail=tail.next
    tail1=tail
    temp2=tail.next
    tail.next=None
    p2=reverse(temp1)
    #print('printing p2 and temp1')
    #please_print(p2)
    #please_print(temp1)
    #print('printing temp2')
    #please_print(temp2)
    p1=recurse(temp2,k1-k,k)
    temp1.next=p1
    #print('printing temp1')
    #please_print(temp1)
    return tail1

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tempor=head
        n=0
        while(tempor):
            n+=1
            tempor=tempor.next
        return recurse(head,n,k)