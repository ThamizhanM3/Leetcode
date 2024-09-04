"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.opt = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.opt.append(root.val)
        if root.children:
            for i in root.children:
                self.preorder(i)
        return self.opt