class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num,0) + 1

        max_heap = [(-freq, num) for (num, freq) in freqs.items()]
        heapq.heapify(max_heap)
        print(max_heap)
        results = []
        i = 0
        while i < k and max_heap:
            freq, num = heapq.heappop(max_heap)
            results.append(num)
            i += 1

        return results