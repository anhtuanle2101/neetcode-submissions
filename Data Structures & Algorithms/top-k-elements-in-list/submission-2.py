class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()

        for num in nums:
            d[num] = d.get(num, 0) + 1

        max_heap = []
        for num, count in d.items():
            heapq.heappush(max_heap,(-count, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res