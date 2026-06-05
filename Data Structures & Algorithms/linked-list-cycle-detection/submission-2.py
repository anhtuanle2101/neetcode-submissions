# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
- small len(linked list)
- cycle detection
    - visited set O(n) space
    - fast, slow pointers O(1) space <---
        - slow pointer moves by 1 node each time
        - fast pointer moves by 2 nodes each time
        - since if the linked list is a straight line, fast will never be able to catch the slow node
        - slow, fast and fast.next is not None each iteration
        - if fast catch slow which means fast and slow points to the same node (fast == slow) return True
        - else return False 

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.
- cycle def

index determines the index of the beginning of the cycle, if it exists
The tail node of the list will set it's next pointer to the index-th node. 
If index = -1, then the tail node points to null and no cycle exists.
index is not given to you as a parameter.
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

        