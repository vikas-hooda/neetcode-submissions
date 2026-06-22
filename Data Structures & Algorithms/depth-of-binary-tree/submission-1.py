# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[root]
        ans=0
        while q:
            nq=[]
            ans+=1
            while q:
                nq.append(q.pop(0))
            for n in nq:
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
        return ans