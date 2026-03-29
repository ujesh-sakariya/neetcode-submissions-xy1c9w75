# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
        if head == None:
            return None 
       

        p = None
        c = head
        temp = None # temporarily store the next node
    
      
        while c: # while c exist ( not pointing to null)
            
            temp = c.next # save the next node
            c.next = p # reverse
            
            # order for next iteration 
            p = c
            c = temp
    
        return p

        