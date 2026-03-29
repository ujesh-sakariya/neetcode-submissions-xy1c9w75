# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        s,f = head,head
        prev = dummy

        while n !=1:

            f = f.next
            n -=1
        
        print(s.val)
        print(f.val)
        
        while f.next != None:
            prev = s
            s = s.next
            f = f.next

        prev.next = s.next

        return dummy.next


        



        