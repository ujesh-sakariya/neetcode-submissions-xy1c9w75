# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hash = {}
        c= head
        index = -1

        while c:


            index += 1 
            if c not in hash:
                hash[c] = index
            else:
                index = hash[c]
                return True

            c = c.next
        
        return False




        