# question link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = deque([])
        if root.left:
            q.append(root.left)
            s = root.left
            if root.right:
                q.append(root.right)
        elif root.right:
            q.append(root.right)
            s = root.right
        sol = []
        cum = root.val
        cnt = 1
        if not q:
            return [root.val]
        while q:
            e = q.popleft()
            if e == s:
                sol.append(cum / cnt)
                cum = e.val
                cnt = 1
                if e.left:
                    s = e.left
                elif e.right:
                    s = e.right
                else:
                    s = None
            else:
                cum += e.val
                cnt += 1
                if not s:
                    if e.left:
                        s = e.left
                    elif e.right:
                        s = e.right
            if e.left:
                q.append(e.left)
            if e.right:
                q.append(e.right)
        sol.append(cum / cnt)
        return sol
