# question link: http://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sol = []
    def doTraversal(self, root, voyage):
        if not root:
            return True
        if root.val != voyage[-1]:
            return False
        val = voyage.pop()
        if not root.left:
            return self.doTraversal(root.right, voyage)
        if root.left.val != voyage[-1]:
            if not root.right:
                return False
            elif root.right.val == voyage[-1]:
                tmp = root.right
                root.right = root.left
                root.left = tmp
                self.sol.append(val)
            else:
                return False
        return self.doTraversal(root.left, voyage) and self.doTraversal(root.right, voyage)
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        voyage = voyage[::-1]
        if not self.doTraversal(root, voyage):
            return [-1]
        return self.sol
