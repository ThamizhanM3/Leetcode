# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    q = []
    a = []
    def __init__(self):
        self.q = []
        self.a = []
    def levelOrder(self, root):
        self.q.append(root)
        while len(self.q):
            x = []
            for i in range(len(self.q)):
                if self.q[0].left:
                    self.q.append(self.q[0].left)
                if self.q[0].right:
                    self.q.append(self.q[0].right)
                x.append(self.q[0].val)
                self.q.pop(0)
            self.a.append(x)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.levelOrder(root)
        print(self.a)
        return self.a[-1][0]