# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative dfs stack
        stack = []  # node, depth
        if root:
            stack.append([root, 1])
        res = 0
        while stack:
            for i in range(len(stack)):
                node, depth = stack.pop()
                if node.left:
                    stack.append([node.left, depth+1])
                if node.right:
                    stack.append([node.right, depth+1])
                res = max(res, depth)
        return res



















        #bfs  tc=sc=O(n)
        if not root:
            return 0

        q=deque([root])
        level=0
        while q:  
          for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
          level+=1
          print(level)
                    
        return level




        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))