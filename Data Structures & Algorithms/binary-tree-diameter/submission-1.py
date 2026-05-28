# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                lefth, leftd = mp[node.left]
                righth, rightd = mp[node.right]

                mp[node] = (1 + max(lefth, righth), max(lefth+righth, leftd, rightd))
        return mp[root][1]















        # dfs  tc=O(n)  sc=O(h)
        res = [0]
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            print("left", left)
            right = dfs(node.right)
            res[0] = max(res[0], left+right)
            return 1 + max(left, right)
        dfs(root)
        return res[0]
