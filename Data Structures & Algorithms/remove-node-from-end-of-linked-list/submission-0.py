# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        c=head
        while c:
            l+=1
            c=c.next
        if n==l:
            return head.next
        f=None
        h=head
        for i in range(n):
            f=h
            h=h.next
        print(f.val)
        p=None
        h=head
        while f.next:
            p=h
            h=h.next
            f=f.next
        print(p.val)
        p.next=p.next.next
        return head
