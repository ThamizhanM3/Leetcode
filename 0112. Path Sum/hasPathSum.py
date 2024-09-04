# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, s, t):
        if not root:
            return False
        if s + root.val == t and not root.left and not root.right:
            return True
        x = False
        if root.left:
            if self.check(root.left, s+root.val, t):
                return True
        if root.right:
            if self.check(root.right, s+root.val, t):
                return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.check(root, 0, targetSum) 