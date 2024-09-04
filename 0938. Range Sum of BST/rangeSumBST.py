# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tot = 0
    def find(self, root, low, high):
        if root != None:
            if root.val >= low and root.val <= high:
                self.tot += root.val
            if root.val > low:
                self.find(root.left, low, high)
            if root.val < high:
                self.find(root.right, low, high)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.find(root, low, high)
        return self.tot