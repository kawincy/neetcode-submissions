# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res, dummy = self.DFS(root)
        return res

    def DFS(self, root):
        if not root:
            return True, -1
        leftBal, leftHeight = self.DFS(root.left)
        rightBal, rightHeight = self.DFS(root.right)
        height = 1 + max(leftHeight, rightHeight)
        balFactor = leftHeight - rightHeight
        bal = leftBal and rightBal and abs(balFactor) < 2
        return bal, height
        