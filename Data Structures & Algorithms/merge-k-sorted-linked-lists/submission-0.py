# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1,l2):

            c = ListNode() 
            start = c
            while l1 != None and l2 != None:

                if l1.val <= l2.val:

                    c.next = l1
                    l1 = l1.next 

                else:

                    c.next = l2
                    l2 = l2.next
                
                c = c.next
            
            if l1 == None:
                c.next = l2
            elif l2 == None:
                c.next = l1
            
            return start.next
        
        print(lists)
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            while len(lists) > 1:
                lists[0:2] = [(merge(lists[0],lists[1]))]
            return lists[0]


        


