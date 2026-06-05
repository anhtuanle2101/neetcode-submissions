# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # cur1 and cur2 are start of list1 and list2 respectively

        # until one of the list exhaust 
        # compare values at cur1 and cur2 
        # which are smaller, put it into the merged list
        # after the loop, if the list1 still has element
        # append the rest of list1, similar to list2

        cur1, cur2 = list1, list2

        def add_node(head, node):
            print(node.val)
            if not head:
                head = node
                return head

            cur = head
            while cur.next:
                cur = cur.next
            
            cur.next = node
            return head

        merged_head = None

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tmp = cur1.next
                cur1.next = None
                merged_head = add_node(merged_head, cur1)
                cur1 = tmp
            else:
                tmp = cur2.next
                cur2.next = None
                merged_head = add_node(merged_head, cur2)
                cur2 = tmp
            
        while cur1:
            tmp = cur1.next
            cur1.next = None
            merged_head = add_node(merged_head, cur1)
            cur1 = tmp
        while cur2:
            tmp = cur2.next
            cur2.next = None
            merged_head = add_node(merged_head, cur2)
            cur2 = tmp

        return merged_head


        