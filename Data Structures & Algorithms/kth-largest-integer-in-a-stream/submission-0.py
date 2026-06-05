class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        heapq.heapify(self.heap)
        
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        result = None
        i = 0
        temp_arr = []
        while True:
            i += 1
            cur = -heapq.heappop(self.heap)
            temp_arr.append(cur)
            if i == self.k:
                result = cur
                break
        for item in temp_arr:
            heapq.heappush(self.heap, -item)
            
        return result
