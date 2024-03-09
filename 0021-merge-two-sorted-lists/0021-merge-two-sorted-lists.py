# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(not list1):
            return list2
        if(not list2):
            return list1
        p1=list1
        p2=list2
        if(list1.val < list2.val):
            head=list1
            tail=list1
            p1=p1.next
        else:
            head=list2
            tail=list2
            p2=p2.next
        while(p1 and p2):
            if(p1.val < p2.val):
                tail.next=p1
                p1=p1.next
            else:
                tail.next=p2
                p2=p2.next
            tail=tail.next
        if(p1):
            tail.next=p1
        if(p2):
            tail.next=p2
        return head
        