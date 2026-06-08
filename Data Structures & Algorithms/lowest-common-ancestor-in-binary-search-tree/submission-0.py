# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def traverse(node, p, q):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node

            left = traverse(node.left, p, q)
            right = traverse(node.right, p, q)


            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right



        return traverse(root, p, q)