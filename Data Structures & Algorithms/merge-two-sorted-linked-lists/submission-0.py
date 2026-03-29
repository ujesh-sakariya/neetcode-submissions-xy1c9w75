# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None:
            return list2
        if list2 == None:
            return list1

        p = None
        while list1 != None and list2 != None:

            if list1.val <= list2.val:

                if p:
                    p.next = list1
                    p = p.next
                else:
                    p = list1
                    h = p
                    
                list1 = list1.next
            else:
                if p:
                    p.next = list2
                    p = p.next
                else:
                    p = list2
                    h = p

                list2 = list2.next
            
            print(p.val)

        # we have reached the end of one list at least
        if list1 == None:
            p.next = list2
        if list2 == None:
            p.next = list1
        
        print(p.val)

        return h

        
        
        

                
        