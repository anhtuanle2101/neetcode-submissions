"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = dict()

        cur = head

        while cur:
            copy_node = Node(cur.val)
            original_to_copy[cur] = copy_node

            cur = cur.next

        cur = head
        while cur:
            referenced_node = original_to_copy[cur]
            referenced_node.next = original_to_copy[cur.next] if cur.next is not None else None
            referenced_node.random = original_to_copy[cur.random] if cur.random is not None else None

            cur = cur.next

        return original_to_copy[head] if head is not None else None
