# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = []
        
    def path(self, root, s):
        if root.left:
            self.path(root.left, s + str(root.val) + '->')
        if root.right:
            self.path(root.right, s + str(root.val) + '->')
        if not root.left and not root.right:
            self.a.append(s + str(root.val))

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left:
            self.path(root.left, str(root.val) + '->')
        if root.right:
            self.path(root.right, str(root.val) + '->')
        if not root.left and not root.right:
            self.a.append(str(root.val))
        return self.a
        