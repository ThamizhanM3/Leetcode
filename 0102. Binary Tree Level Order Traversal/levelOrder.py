# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.q = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            self.q.append(root)
        opt = []
        while len(self.q):
            x = []
            n = len(self.q)
            for j in range(n):
                i = self.q.pop(0)
                x.append(i.val)
                if i.left:
                    self.q.append(i.left)
                if i.right:
                    self.q.append(i.right)
            opt.append(x)
        return opt