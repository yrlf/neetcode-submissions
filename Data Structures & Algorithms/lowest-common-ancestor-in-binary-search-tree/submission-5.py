# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def lca(root, p, q):
            if root == None:
                return None

            if root.val == p.val or root.val == q.val:
                return root
            

            ans = None      
            if p.val > root.val and q.val > root.val:
                ans = lca(root.right, p, q)
            elif p.val < root.val and q.val < root.val:
                ans = lca(root.left, p,  q)
            else:
                ans = root
            
            return ans
        

        return lca(root, p, q)

