class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        # each iteration, take two most heaviest stones that would take 2 log n to do so
        # if two stones are equal, continue
        # else get what left when two stones are smashed together and put it back to the heap
        # repeat until there is one stone left
        # return the last remaining stone or 0 if there is no stone left

        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            left = abs(stone1 - stone2)

            if left == 0:
                continue    
            heapq.heappush(max_heap, -left)
        
        return -max_heap[0] if len(max_heap) > 0 else 0
                