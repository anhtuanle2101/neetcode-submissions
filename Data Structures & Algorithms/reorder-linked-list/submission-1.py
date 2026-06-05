# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        second = self.reverse(second)
        cur1, cur2 = head, second
        while cur2:
            tmp1, tmp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = tmp1
            cur1, cur2 = tmp1, tmp2

    def reverse(self, head):
        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev