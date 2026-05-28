# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        parent = None
        cur = root

        # find the node to delete
        while cur and cur.val!=key:
            parent = cur
            if key>cur.val:
                cur = cur.right
            else:
                cur = cur.left
            
        if not cur:
            return root
        
        # Node with only one child or no child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left==cur:
                parent.left = child
            else:
                parent.right = child
        else:
            # Node with two children
            par = None
            delNode= cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left
            
            if par:
                par.left = cur.right
                cur.right = delNode.right
            
            cur.left = delNode.left

            if not parent:
                return cur
            
            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur
        return root
        
        
        
        
        
        # if not root:
        #     return root
        
        # if key>root.val:
        #     root.right = self.deleteNode(root.right, key)
        # elif key<root.val:
        #     root.left = self.deleteNode(root.left, key)
        # else:
        #     if not root.left:
        #         return root.right
        #     elif not root.right:
        #         return root.left
            
        #     cur = root.right
        #     while cur.left:
        #         cur = cur.left
        #     root.val = cur.val
        #     root.right = self.deleteNode(root.right, root.val)
        # return root













