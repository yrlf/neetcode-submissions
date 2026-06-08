# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def t(p, q):
            # if not((not p and not q) or (p.val == q.val)):
            #     return False
            if  not p and not q:
                return True

            if (not p and q) or (not q and p) or (p.val != q.val):
                return False

            res = True

            return res and t(p.left, q.left) and t(p.right, q.right)
        
        return t(p,q)