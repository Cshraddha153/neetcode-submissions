# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return True, 0
            left_b, left = dfs(node.left)
            right_b, right = dfs(node.right)
            balanced = left_b and right_b and abs(left-right)<=1 
            height = 1+max(left, right)
            return balanced, height
        return dfs(root)[0]