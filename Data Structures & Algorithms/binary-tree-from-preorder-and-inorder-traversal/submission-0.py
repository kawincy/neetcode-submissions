# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(val = preorder[0]);
        if len(preorder) == 1:
            return root
        midPointer = 0
        while inorder[midPointer] != root.val:
            midPointer += 1

        leftInorder = inorder[0:midPointer]
        leftPreorder = preorder[1 : 1 + len(leftInorder)]
        root.left = self.buildTree(leftPreorder, leftInorder)

        rightInorder = inorder[midPointer + 1 : len(inorder)]
        rightPreorder = preorder[1 + len(leftInorder) : len(preorder)]
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root
        