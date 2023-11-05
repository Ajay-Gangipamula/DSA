# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=None
        tmp=head
        while(tmp):
            p=tmp.next
            tmp.next=curr
            curr=tmp
            tmp=p
        return curr