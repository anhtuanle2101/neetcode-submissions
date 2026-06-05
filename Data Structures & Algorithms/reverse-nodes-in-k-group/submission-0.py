# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # take kth nodes and reverse at a time, 
        # keep track of the next start of the next group of k nodes
        # while taking kth nodes if we reach the end, just stop the loop
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth_node = self.getNextKthNode(group_prev, k)
            if not kth_node:
                break
            
            group_next = kth_node.next

            # start reversing the k nodes
            prev, cur = kth_node.next, group_prev.next

            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = group_prev.next
            group_prev.next = kth_node
            group_prev = tmp
        return dummy.next

    def getNextKthNode(self, cur, k):
        while cur and k > 0:
            k -= 1
            cur = cur.next
            
        return cur