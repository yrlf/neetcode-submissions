# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found = False

        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)


        def t(root, subRoot):
            nonlocal found
            if isSame(root, subRoot):
                found = True
                return
            if root.left:
                t(root.left, subRoot)
            if root.right:
                t(root.right, subRoot)

        t(root, subRoot)

        return found