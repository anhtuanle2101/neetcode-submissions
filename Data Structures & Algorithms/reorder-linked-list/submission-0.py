# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        while cur.next:
            # get the node before tail
            previous_tail = cur
            while previous_tail.next.next:
                previous_tail = previous_tail.next
            
            # get the tail node, set the next of previous tail node to None
            tail = previous_tail.next
            previous_tail.next = None

            # put the tail node after the current node and before the next node of current node
            tmp = cur.next
            cur.next = tail
            tail.next = tmp
            if tmp is None:
                break
            cur = cur.next.next

        return head