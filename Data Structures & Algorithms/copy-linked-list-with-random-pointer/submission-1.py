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
        # create a hash map OldToCopy where key being the
        # old object and the value being the copy of the
        # corresponding node,
        # traverse through the list, check
        # for each node, create a copy of the node,
        # map the old node to this copy node

        # another loop through the list, now connect
        # the random node by getting the copy of corresponding node
        # in the map
        if not head:
            return
        oldToCopy = dict()

        cur = head
        while cur:
            copyNode = Node(cur.val)
            oldToCopy[cur] = copyNode
            cur = cur.next
        cur = head
        while cur:
            copyNode = oldToCopy[cur]

            if cur.next:
                copyNode.next = oldToCopy[cur.next]
            if cur.random:
                copyNode.random = oldToCopy[cur.random]

            cur = cur.next
        
        return oldToCopy[head]
