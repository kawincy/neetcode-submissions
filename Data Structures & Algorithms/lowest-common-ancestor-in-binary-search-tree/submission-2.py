# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = min(p.val, q.val)
        right = max(p.val, q.val)
        curr = root
        while not (curr.val > left and curr.val < right):
            if curr.val == left or curr.val == right:
                return curr
            if curr.val > right:
                curr = curr.left
            elif curr.val < left:
                curr = curr.right
        return curr


        