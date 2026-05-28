# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def traversal(node):
            if not node:
                return
            arr.append(node.val)
            traversal(node.left)
            traversal(node.right)
        
        traversal(root)
        arr.sort()
        return arr[k-1]

















        # tc = O(n)  sc=O(n)  iterative dfs
        stack = []
        cur = root
        n=0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur = cur.right
