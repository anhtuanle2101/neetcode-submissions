class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    ## use double linked list with two dummy left and right pointers
    # write helper functions for insert a node at the end 
    # and remove a node anywhere in the list
    # make use of a hash map to keep track key -> node
    # Get: check if key exists in the map if yes, 
    # move the node to be recently used by remove the node and 
    # insert it back to the end of the list
    # and return the value, otherwise return -1
    # Put: if the key exists in the map, initially remove it
    # from the list, then does not matter it exists in the 
    # map or not, reassign the value and put it back
    # to the end of the list
    # check if the size exceeds the capacity, if yes,
    # remove the head node and corresponding element in the map
    def __init__(self, capacity: int):
        self.m = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity

    def insert(self, node):
        node.prev, node.next = self.right.prev, self.right
        node.prev.next = self.right.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m.get(key)
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m.get(key)
            self.remove(node)
        self.m[key] = Node(key, value)
        self.insert(self.m[key])

        if len(self.m) > self.capacity:
            head = self.left.next
            self.remove(head)
            del self.m[head.key]
        
