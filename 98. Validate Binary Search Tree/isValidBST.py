# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, ll, ul):
        if not root:
            return True
        if root.val >= ul or root.val <= ll:
            return False
        else:
            return self.check(root.left, ll, root.val) and self.check(root.right, root.val, ul)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, -inf, root.val) and self.check(root.right, root.val, inf)