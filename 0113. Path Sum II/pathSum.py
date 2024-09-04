# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, s, t):
        if not root:
            return
        if sum(s) + root.val == t and not root.left and not root.right:
            self.a.append(s+[root.val])
        if root.left:
            self.check(root.left, s+[root.val], t)
        if root.right:
            self.check(root.right, s+[root.val], t)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.a = []
        self.check(root, [], targetSum)
        return self.a
        