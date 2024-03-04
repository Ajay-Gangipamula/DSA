# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
        while(h and t):
            tail.next=t
            t=t.next
            tail=tail.next
            tail.next=h
            h=h.next
            tail=tail.next
            tail.next=None