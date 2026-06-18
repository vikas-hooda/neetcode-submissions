# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s=head
        f=head.next
        while f:
            if f==s:
                return True
            f=f.next
            if f:
                f=f.next
            s=s.next
        return False