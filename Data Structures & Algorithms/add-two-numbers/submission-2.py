# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get two numbers from each list
        # add them together
        # get the remainder of the number mod 10 and create
        # a node of this value and add it to the result list
        # carry over will be the result of the sum integer divide by 10
        # go to the next two numbers
        # check each list if there is still numbers to be added
        # sum each number with carry over value and calculate
        # the next nubmer and next carry over

        num1, num2 = l1, l2
        carry = 0

        result = None
        cur_result = result
        while num1 and num2:
            total = num1.val + num2.val + carry

            carry = total // 10
            print(total % 10)
            new_node = ListNode(total % 10)

            if not result:
                cur_result = new_node
                result = cur_result
            else:
                cur_result.next = new_node
                cur_result = cur_result.next
                
            num1 = num1.next
            num2 = num2.next

        while num1:
            total = num1.val + carry
            print(total % 10)
            carry = total // 10
          
            new_node = ListNode(total % 10)

            if not result:
                cur_result = new_node
                result = cur_result
            else:
                cur_result.next = new_node
                cur_result = cur_result.next

            num1 = num1.next
        
        while num2:
            total = num2.val + carry

            carry = total // 10
            
            new_node = ListNode(total % 10)

            if not result:
                cur_result = new_node
                result = cur_result
            else:
                cur_result.next = new_node
                cur_result = cur_result.next

            num2 = num2.next
        
        if carry > 0:
            new_node = ListNode(carry)

            cur_result.next = new_node

        return result
            