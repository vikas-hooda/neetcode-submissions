# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ans=ListNode()
        c=0
        while l1 or l2 or c:
            t=c
            if l1:
                t=t+l1.val
                l1=l1.next
            if l2:
                t+=l2.val
                l2=l2.next
            c=t//10
            t=t%10
            ans.next=ListNode(t)
            ans=ans.next
        return dummy.next