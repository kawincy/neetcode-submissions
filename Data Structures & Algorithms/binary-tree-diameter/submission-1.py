# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter, height = self.DFS(root, 0)
        return diameter

    def DFS(self, root, diameter) -> int:
        if not root:
            return diameter, 0
        diameter, leftH = self.DFS(root.left, diameter)
        diameter, rightH = self.DFS(root.right, diameter)
        height = 1 + max(leftH, rightH)
        diameter = max(leftH + rightH, diameter)
        return diameter, height


        