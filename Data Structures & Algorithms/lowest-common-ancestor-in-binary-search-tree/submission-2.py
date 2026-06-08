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
            
            
            
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)
            if left and right:
                return root
            if left:
                return left
            else:
                return right
        

        return lca(root, p, q)

