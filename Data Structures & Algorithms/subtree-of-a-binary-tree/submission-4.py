# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subroot):
            if root == subroot == None: return True
            if not (root and subroot): return False
            if root.val != subroot.val:
                # print(' i got called')  
                # print(root.val, subroot.val)  
                return False
            return sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right)

        q = deque()
        q.append(root)
        while q:
            curr = q.pop()
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)

            if curr.val == subRoot.val:
                if sameTree(curr, subRoot): return True

        return False


