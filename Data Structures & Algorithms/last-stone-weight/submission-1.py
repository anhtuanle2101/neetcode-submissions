'''
    stones[i] ith stone weight
    - loop until one stone remaining
        - get two heaviest stones x and y
            - if x == y, both stones are destroyed
            - if x > y, y is destroyed, x - y stone is left and put it back to the list

    - max_heap -> O(logn) to get the max stone O(n) to heapify the stones
        - at each iteration, condition len(stones) >= 2
            - get two heavies stones x and y
                - x == y
                    continue
                - if x < y => x, y = y, x
                    now x > y, ignore y and put the stone with weight x - y back to the list
        
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-w for w in stones]

        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if x == y:
                continue

            if y > x:
                x, y = y, x

            # x > y
            left = x - y
            heapq.heappush(max_heap, -left)

        return -max_heap[0] if len(max_heap) == 1 else 0