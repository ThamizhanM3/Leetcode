# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, p, q):
        x1 = True
        x2 = True
        if p.val != q.val:
            return False
        if (p.left and not q.left) or (p.right and not q.right) or (q.left and not p.left) or (q.right and not p.right):
            return False 
        if p.left and q.left:
            x1 = self.check(p.left, q.left)
        if p.right and q.right:
            x2 = self.check(p.right, q.right)
        return x1 and x2 and p.val == q.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True
        if (p == None and q != None) or (q == None and p != None):
            return False
        return self.check(p, q) 