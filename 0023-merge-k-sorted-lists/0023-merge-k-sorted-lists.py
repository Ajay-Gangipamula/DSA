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

def mergek(lists,i,j):
    if(i==j):
        return lists[i]
    m=(i+j)//2
    l1=mergek(lists,i,m)
    l2=mergek(lists,m+1,j)
    return merge(l1,l2)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists)==0):
            return None
        return mergek(lists,0,len(lists)-1)