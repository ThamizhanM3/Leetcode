# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    arr = []
    def search(self, root):
        if root!= None:
            if root.left != None:
                self.search(root.left)
            if root.right != None:
                self.search(root.right)
            if root.left == None and root.right == None:
                self.arr.append(root.val)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.arr = []
        self.search(root1)
        a = []
        a = self.arr.copy()
        self.arr = []
        self.search(root2)
        print(a, self.arr)
        if a == self.arr:
            return True
        return False