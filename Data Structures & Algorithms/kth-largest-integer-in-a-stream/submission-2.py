class KthLargest:

    '''
        heap -> O(n) to heapify the nums 
    '''
    def __init__(self, k: int, nums: List[int]):
        self.heap = [num for num in nums]
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    '''
        append val to the DS and return kth largest int
        - heap -> log(n) to return max value
            -> k log(n) to return kth largest -> optimal
    '''
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
