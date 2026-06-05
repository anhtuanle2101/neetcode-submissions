# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = cur_result = ListNode()
        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if ((cur1.val <= cur2.val)):
                cur_result.next = cur1
                cur1 = cur1.next
            elif ((cur1.val > cur2.val)):
                cur_result.next = cur2
                cur2 = cur2.next
            cur_result = cur_result.next

        cur_result.next = cur1 or cur2
        return result.next