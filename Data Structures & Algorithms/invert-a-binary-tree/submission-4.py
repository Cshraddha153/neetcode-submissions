# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS SOLUTION  TC=O(N)   S.C=O(N)  iterative dfs
        if not root:
            return None
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
            



        # BFS ==>  TC = O(N)  AND  SC = O(N)
        #base case
        if not root:
            return None
        q = deque([root])
        while q:
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


        # DFS SOLUTION  TC=O(N)   S.C=O(N)  recursive stack
        #base case
        if not root:
            return None
       
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

        