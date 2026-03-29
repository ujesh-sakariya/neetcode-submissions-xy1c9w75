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

        if not head:
            return None
        
        ds = {}
        copy = head
       
        while head:

            ds[head] = Node(head.val)
            head = head.next
        
        c2 = copy
        while copy:
            ds[copy].next = ds.get(copy.next)
            ds[copy].random = ds.get(copy.random)
            copy = copy.next
        return ds[c2]

        

        
        