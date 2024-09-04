# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.n1 = []
        self.n2 = []
        self.n = []
        self.ck = False

    def path(self, root, n, arr):
        if self.ck:
            return
        arr.append(root)
        if root == n:
            self.ck = True
            if len(self.n1):
                self.n2 = arr.copy()
            else:
                self.n1 = arr.copy()
            return
        if root.left:
            self.path(root.left, n, arr.copy())        
        if root.right:
            self.path(root.right, n, arr.copy())        


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path(root, p, [])
        self.ck = False
        self.path(root, q, [])
        i = 0
        while i < min(len(self.n1), len(self.n2)):
            if self.n1[i] == self.n2[i]:
                i += 1
            else:
                return self.n1[i-1]
        return self.n1[min(len(self.n1), len(self.n2))-1]