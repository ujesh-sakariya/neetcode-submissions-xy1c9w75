# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s = head # slow pointer 
        f = head # fast pointer

        while f and f.next: #not reached the end ( remeber there is a null node )

            f = f.next.next
            s = s.next

            if f == s:

                return True
            
        return False

    
        





        