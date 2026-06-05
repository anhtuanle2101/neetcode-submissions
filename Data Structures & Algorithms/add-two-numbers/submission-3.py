# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0) 
        cur_res = dummy
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
            if l2:
                total += l2.val

            total += carry

            next_res = total % 10
            carry = total // 10

            cur_res.next = ListNode(next_res)
            cur_res = cur_res.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        if carry:
            cur_res.next = ListNode(carry)

        return dummy.next