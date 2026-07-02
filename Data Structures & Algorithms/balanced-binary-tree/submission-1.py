# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isb(n):
            if not n:
                return True, 0
            lb,lh=isb(n.left)
            rb,rh=isb(n.right)
            return lb and rb and (abs(lh-rh)<=1) , 1 + max(lh,rh)
        return isb(root)[0]