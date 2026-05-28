# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, float('-inf'))])
        res = 0
        while q:
            for i in range(len(q)):
                node, prev = q.popleft()
                
                if node.val>=prev:
                    res+=1
                new_prev = max(prev, node.val)
                if node.left:
                    q.append((node.left, new_prev))
                if node.right:
                    q.append((node.right, new_prev))
        return res




        # tc=O(N)   sc=O(N)
        # def dfs(node, prev):
        #     if not node:
        #         return 0
            
        #     is_good = 1 if node.val >= prev else 0
        #     new_max = max(prev, node.val)
        #     return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)
            

        # return dfs(root, float("-inf"))