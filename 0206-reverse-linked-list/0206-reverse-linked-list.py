# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def recurse(p):
    if(p is None or p.next is None):
        return p
    temp=p.next
    p.next=None
    head1=recurse(temp)
    temp.next=p
    #p.next=head1
    return head1

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head
        head3=recurse(head)
        return head3
        return recurse(head)