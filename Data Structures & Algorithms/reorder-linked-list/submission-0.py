# headDefinition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        s,f = head,head.next # pointers to find the middle of a list

        while f and f.next:
            s = s.next
            f = f.next.next
        
        # s will be the middle element 
    

        # now we need to reverse the second half of the list
        p,c = None,s.next
        s.next = None # disconnect the first list from the second
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        
        # merging the 2 lists together now 
        l1 = head
        l2 = p 

        while l1 and l2:

            print(l1.val,l2.val)
            t1 = l1.next
            l1.next = l2
            l1 = t1
            t2 = l2.next
            l2.next = l1
            l2 = t2
        
        return 
        





        