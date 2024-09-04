# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tot = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root.left != None and root.left.left == None and root.left.right == None:
            self.tot += root.left.val
        if root.left != None:
            self.sumOfLeftLeaves(root.left)
        if root.right != None:
            self.sumOfLeftLeaves(root.right)
        return self.tot