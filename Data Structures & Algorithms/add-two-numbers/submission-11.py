# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        ans = l2
        while l1 and l2:
            prev = l2
            if l1.val + l2.val + carry < 10:
                l2.val = l1.val + l2.val + carry
                carry = 0
            else:
                temp = l2.val
                l2.val = (l1.val + l2.val  + carry ) % 10
                carry =  (l1.val + temp + carry) // 10
            l1 = l1.next
            l2 = l2.next
            print(carry)
                
        if l1 == None and l2:
            prev = l2
            temp = l2.val
            l2.val = (l2.val + carry ) % 10
            carry =  (temp + carry) // 10
            l2 = l2.next
            if carry !=0:
                prev.next = ListNode(carry)
        elif l2 == None and l1:
            while l1:
                prev.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                prev = prev.next
            if carry !=0:
                prev.next = ListNode(carry)
        else:
            if carry !=0:
                print('y')
                prev.next = ListNode(carry)
        
        return ans



