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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid=getMid(head)
        t=reverse(mid)
        h=head
        while(t and h):
            if(t.val!=h.val):
                return False
            t=t.next
            h=h.next
        return True