# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None


def execute():
    tail=LinkedList(4)
    tail.next=LinkedList(5)
    tail.next.next=LinkedList(7)
    print("printing tail")
    please_print(tail)
    temp=tail
    print("printing temp")
    please_print(temp)
    h=LinkedList(785)
    temp.next=h
    please_print(temp)
    please_print(tail)

def getMid(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    return slow

def reverse(p):
    curr=p
    prev=None
    while(curr):
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

def please_print(tmp):
    #print("printing head")
    while(tmp):
        print(tmp.val,"->",end=" ")
        tmp=tmp.next
    print()

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp=head
        mid=getMid(temp)
        t=reverse(mid)
        h=temp.next
        tail=head
        print("printing tail")
        please_print(tail)
        while(h and t):
            tail.next=t
            t=t.next
            tail=tail.next
            tail.next=h
            h=h.next
            tail=tail.next
            tail.next=None