"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        dic = {None:None}
        while cur:
            copy = Node(cur.val)
            dic[cur] = copy
            cur = cur.next
        print(dic)

        cur=head
        while cur:
            node = dic[cur]
            node.next = dic[cur.next]
            node.random = dic[cur.random]
            cur = cur.next
        
        return dic[head]















