# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p = ListNode() # create a dummy node
        start = p # store this so we have ref to start of linked list
        while list1 != None and list2 != None:

            if list1.val <= list2.val:

                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
               
                
            
            print(p.val)

        # we have reached the end of one list at least
        if list1 == None:
            p.next = list2
        if list2 == None:
            p.next = list1
        
        print(p.val)

        return start.next # so we skip the dummy node ( it is just in space)

        
        
        

                
        