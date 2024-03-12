"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head):
            return None
        clonehead=Node(head.val)
        tmp=clonehead
        head1=head
        d={head1:tmp}
        head1=head1.next
        while(head1):
            p=Node(head1.val)
            d[head1]=p
            tmp.next=p
            tmp=tmp.next
            head1=head1.next
        tmp=clonehead
        head1=head
        while(head1 and tmp):
            if(head1.random):
                tmp.random=d[head1.random]
            else:
                tmp.random=None
            head1=head1.next
            tmp=tmp.next
        return clonehead