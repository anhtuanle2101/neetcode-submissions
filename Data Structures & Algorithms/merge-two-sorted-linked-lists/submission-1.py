# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_result = None
        result = cur_result
        cur1, cur2 = list1, list2

        while cur1 or cur2:
            if (((cur1 and cur2) and cur1.val <= cur2.val) or (cur1 and not cur2)):
                tmp = cur1.next
                cur1.next = None
                if not cur_result:
                    cur_result = cur1
                    result = cur_result
                else:
                    cur_result.next = cur1
                    cur_result = cur_result.next
                cur1 = tmp
            elif (((cur1 and cur2) and cur1.val > cur2.val) or (cur2 and not cur1)):
                tmp = cur2.next
                cur2.next = None
                if not cur_result:
                    cur_result = cur2
                    result = cur_result
                else:
                    cur_result.next = cur2
                    cur_result = cur_result.next
                cur2 = tmp
        return result