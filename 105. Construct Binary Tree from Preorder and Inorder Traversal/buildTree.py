# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, prelo, prehi, inlo, inhi, preorder, inorder):
        if prelo > prehi or inlo > inhi:
            return None
        root = ListNode()
        root.val = preorder[prelo]
        idx = inorder.index(preorder[prelo])
        tec = idx-inlo
        root.left = self.construct(prelo+1, prelo+tec, inlo, idx-1, preorder, inorder)
        root.right = self.construct(prelo+tec+1, prehi, idx+1, inhi, preorder, inorder)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.construct(0, len(preorder)-1, 0, len(inorder)-1, preorder, inorder)