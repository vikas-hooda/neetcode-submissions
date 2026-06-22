# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isb(r):
            if not r:
                return 0
            rh=isb(r.right)
            lh=isb(r.left)
            return -1 if (lh==-1 or rh==-1 or abs(lh-rh)>1) else max(lh,rh)+1
        r=isb(root)
        return False if r==-1 else True