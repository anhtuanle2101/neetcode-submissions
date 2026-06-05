# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set prev node initially to None
        # traverse through the list to get the list length
        # traverse the list to the nth element from the end at index (len - n)
        # set prev node to cur.next to remove the nth node
        
        list_len = 0
        cur = head
        while cur:
            cur = cur.next
            list_len += 1

        cur_index = 0
        target_index = list_len - n

        cur = head
        prev = None
        while cur and cur_index <= target_index:

            if cur_index == target_index:
                if prev:
                    prev.next = cur.next
                else:
                    head = head.next
                break
            
            prev = cur
            cur = cur.next
            cur_index += 1
            
        return head