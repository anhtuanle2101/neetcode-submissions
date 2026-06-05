# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force
        # at each iteration, find the minimum value
        # from each list, then take out this value,
        # and add it to the merged list, do this until
        # all k lists exhaust
        # k * n

        # log(k) * n approach
        # merge lists in pair at each iteration

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                mergedLists.append(self.mergeLists(l1, l2))
            
            lists = mergedLists
        
        return lists[0]

    def mergeLists(self, l1, l2):
        # TODO
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next