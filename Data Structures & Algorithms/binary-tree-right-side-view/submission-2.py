# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs tc=O(n)  sc=O(n)
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if depth==len(res):
                res.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return res











        # bfs tc=sc=O(N)
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append((node.left))
                if node.right:
                    q.append((node.right))
            res.append(node.val)
        return res