# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ist(p,q):
            if not p and not q:
                return True
            if not p or not q or q.val!=p.val:
                return False
            return ist(p.left,q.left) and ist(p.right,q.right)
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val==q.val and ist(p,q):
                return True
            return dfs(p.left,q) or dfs(p.right,q)
        return dfs(root,subRoot)