# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs or preorder traversal of bst and then sorting the traversal order  tc=O(nlogn) sc=O(N)
        # arr = []
        # def traversal(node):
        #     if not node:
        #         return
        #     arr.append(node.val)
        #     traversal(node.left)
        #     traversal(node.right)
        
        # traversal(root)
        # arr.sort()
        # return arr[k-1]


        # inorder traversal which is already in sorted order tc=sc=O(N)
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
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
