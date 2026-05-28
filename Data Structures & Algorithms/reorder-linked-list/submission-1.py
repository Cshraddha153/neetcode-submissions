# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Tc=O(N)  sc=O(N)
        if not head:
            return 

        Nodes = []
        cur = head
        while cur:
            Nodes.append(cur)
            cur = cur.next

        i, j = 0, len(Nodes)-1
        while i<j:
            Nodes[i].next = Nodes[j]
            i+=1
            if i>=j:
                break
            Nodes[j].next = Nodes[i]
            j-=1
            
        Nodes[i].next = None
    

        
