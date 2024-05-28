# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, left, right):
        if left and not right:
            return False
        if not left and right:
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        if left.right and not right.left:
            return False
        if not left.right and right.left:
            return False
        if left.left and not right.right:
            return False
        if left.left and not right.right:
            return False
        return True and self.check(left.right, right.left) and self.check(left.left, right.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)