# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(list1,list2):
    if(not list1):
        return list2
    if(not list2):
        return list1
    if(list1.val < list2.val):
        head=list1
        temp=list1.next
        head.next=None
        head.next=merge(temp,list2)
    else:
        head=list2
        temp=list2.next
        head.next=None
        head.next=merge(list1,temp)
    return head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return merge(list1,list2)