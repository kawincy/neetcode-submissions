# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iterator = iter(preorder)
        indMap = {v : i for i, v in enumerate(inorder) }

        def build(lo, hi):
            root = None
            if lo <= hi:
                value = next(iterator)
                root = TreeNode(val=value)

                ind = indMap[value]

                root.left = build(lo, ind - 1)
                root.right = build(ind + 1, hi)
            return root

        return build(0, len(inorder) - 1)


        