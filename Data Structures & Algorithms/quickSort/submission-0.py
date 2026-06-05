# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quick_sort(pairs, 0, len(pairs) - 1)

        # [3, 2, 3]

        # [3, 2] []
        return pairs


    def quick_sort(self, arr, start, end):
        # base case where len(arr) == 1
        if end - start + 1 <= 1:
            return

        # pick the pivot -> right-most element
        pivot = arr[end]
        # init next element to swap
        nxt = start

        # moving right element from start to end
        # if the element is less or equal to pivot, swap with nxt and move nxt to the next position
        for r in range(start, end):
            if arr[r].key < pivot.key:
                arr[nxt], arr[r] = arr[r], arr[nxt]
                nxt += 1
            
        arr[end], arr[nxt] = arr[nxt], arr[end]
        
        # quick sort on 2 partitions [start:nxt] [nxt:end]
        self.quick_sort(arr, start, nxt - 1)
        self.quick_sort(arr, nxt + 1, end)