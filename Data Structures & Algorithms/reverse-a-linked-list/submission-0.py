# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        if head == None:
            return None 
        if head.next == None:
            return head

        p1,p2 = None,head
        current = head.next # the current node being looked at 
        
        while current.next != None:
            
            p2.next = p1 # reverse
            
            # order for next iteration 
            p1 = p2
            p2 = current
            current = current.next
        
        # final assignment
        current.next = p2
        p2.next = p1

        return current

        