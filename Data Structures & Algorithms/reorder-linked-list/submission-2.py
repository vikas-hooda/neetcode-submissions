# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        def reverse(h):
            p=None
            c=h
            while c:
                t=c.next
                c.next=p
                p=c
                c=t
            return p
        c=head
        l=0
        while c:
            l+=1
            c=c.next
        t=l//2 if l%2 else l//2 -1
        c=head
        while t:
            c=c.next
            t-=1
        h2=c.next
        c.next=None
        h2=reverse(h2)
        h1=head
        while h1 and h2:
            t1 = h1.next
            t2 = h2.next

            h1.next = h2
            h2.next = t1

            h1 = t1
            h2 = t2
        