class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using sort then return the kth largest number could work but result in n log n time
        # using max heap could reduce it to k log n time where k <= n 
        # heapify the nums become a max heap, 
        # for k time, pop each number, at kth time, this is the result
        
        result = None

        max_heap = [-num for num in nums]

        heapq.heapify(max_heap)

        while True:
            if k == 1:
                result = -heapq.heappop(max_heap)
                break
            
            heapq.heappop(max_heap)
            k -= 1
        
        return result