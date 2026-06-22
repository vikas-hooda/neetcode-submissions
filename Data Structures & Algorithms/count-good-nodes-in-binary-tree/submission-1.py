# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(n,m):
            if not n:
                return 0
            ans=1
            if n.val<m:
                ans=0
            m=max(n.val,m)
            return ans+dfs(n.right,m)+dfs(n.left,m)
        return dfs(root,-200)