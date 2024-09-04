# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteThis(self, root):
        if root.right:
            i = root.right
            while i.left:
                i = i.left
            i.left = root.left
            return root.right
        else:
            return root.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            return self.deleteThis(root)
        elif root.left and root.left.val == key:
            root.left = self.deleteThis(root.left)
        elif root.right and root.right.val == key:
            root.right = self.deleteThis(root.right)
        elif key < root.val:
            self.deleteNode(root.left, key)
        elif key > root.val:
            self.deleteNode(root.right, key)
        return root