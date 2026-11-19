# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validSearcher(root, -1001, 1001)
      
    def validSearcher(self, root, left, right):
        if not root:
            return True
        if not (root.val > left and root.val < right):
            return False

        return self.validSearcher(root.left, left, root.val) and\
                self.validSearcher(root.right, root.val, right)
