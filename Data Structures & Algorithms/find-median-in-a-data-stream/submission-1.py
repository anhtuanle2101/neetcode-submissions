class MedianFinder:

    def __init__(self):
        # use two heaps min_heap and max_heap to store the numbers
        # all the numbers in max_heap will be smaller or equals to the all
        # numbers in min_heap, and those two heaps should be approximately equal in length
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # first add the number to max_heap
        heapq.heappush(self.max_heap, -num)
        # ensure the all number in max heap is smaller or equals to all numbers
        # in min heap
        while self.min_heap and self.max_heap and -self.max_heap[0] > self.min_heap[0]:
            cur = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, cur)

        # then now all elements in the max heap is maller or equals to numbers
        # in the min heap, balance out the length of each heaps
        while abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            else:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        print(self.max_heap, self.min_heap)
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        