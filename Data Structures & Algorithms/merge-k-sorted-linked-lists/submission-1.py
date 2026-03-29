# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        

        if len(lists) == 0:
            return None

        def merge(l1,l2):
            c = ListNode() # current node (dummy node used at start)
            s = c
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

            return s.next

            
        def splitList(lists):

            if len(lists) == 1:
                print(lists)
                return lists[0]
            else:
                for l in lists:
                    print (l.val)
                return merge(splitList(lists[:len(lists)//2]),splitList(lists[len(lists)//2:]))

        print(lists)
        return splitList(lists)



        








        


