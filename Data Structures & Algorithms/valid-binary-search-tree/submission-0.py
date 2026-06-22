# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(r,m,n):
            if not r:
                return True
            if r.val>=m or r.val<=n:
                return False
            return dfs(r.left,r.val,n) and dfs(r.right,m,r.val)
        return dfs(root,2000,-2000)