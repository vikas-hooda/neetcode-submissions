# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if not n:
                return 0,0
            lm,ld=dfs(n.left)
            rm,rd=dfs(n.right)
            return 1+max(lm,rm), max(ld,rd,lm+rm)
        return dfs(root)[1]