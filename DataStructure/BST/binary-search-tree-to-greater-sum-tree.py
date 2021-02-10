# question link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = 0
    def visit(self, node):
        node.val += self.prev
        self.prev = node.val
    def reverse_inorder(self, root):
        if not root:
            return
        self.reverse_inorder(root.right)
        self.visit(root)
        self.reverse_inorder(root.left)
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.reverse_inorder(root)
        return root
