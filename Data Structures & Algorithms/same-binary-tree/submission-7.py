# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            valp, valq = stack.pop()
            if valp is None and valq is None:
                continue
            if valp is None or valq is None or valp.val!=valq.val:
                return False
            stack.append((valp.right, valq.right))
            stack.append((valp.left, valq.left))
        return True













        # qp = deque([p])
        # qq = deque([q])
        # while qp and qq:
        #  for _ in range(len(qp)):
        #     valp = qp.popleft()
        #     valq = qq.popleft()
        #     if valp is None and valq is None:
        #         continue
        #     if valp is None or valq is None:
        #         return False
        #     if valp.val!=valq.val:
        #         return False
        #     qp.append(valp.left)
        #     qp.append(valp.right)
        #     qq.append(valq.left)
        #     qq.append(valq.right)
        # return True

            












        
        # dfs  tc and sc = O(n)
        # if not p and not q:
        #     return True
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False
