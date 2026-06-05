# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0 

        cur = head

        while cur:
            size += 1
            cur = cur.next

        pos = size - n + 1

        dummy = ListNode()
        dummy.next = cur = head
        prev = dummy
        cur_pos = 1

        while cur:
            tmp = cur.next
            if cur_pos == pos:
                prev.next = cur.next
                break
            
            cur_pos += 1
            prev, cur = cur, tmp
        
        return dummy.next
            
            


