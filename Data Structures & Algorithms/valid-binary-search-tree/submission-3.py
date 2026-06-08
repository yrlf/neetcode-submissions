# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            if not root.left and not root.right:
                return True, root.val, root.val
            
            leftValid, rightValid = True, True
            leftMin, leftMax, = float('inf'), float('-inf')
            rightMin, rightMax = float('inf'), float('-inf')
            if root.left:
                leftValid, leftMin, leftMax= traverse(root.left)
            if root.right:
                rightValid, rightMin, rightMax = traverse(root.right)

            return (leftValid and rightValid and root.val > leftMax and root.val < rightMin), min(leftMin, rightMin, root.val), max(rightMax, leftMax, root.val)

        
        return traverse(root)[0]