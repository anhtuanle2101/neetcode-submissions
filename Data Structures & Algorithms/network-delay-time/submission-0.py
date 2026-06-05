class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1, n+1)}
        m = {}

        for s, d, w in times:
            adj_list[s].append((d, w))
        
        min_heap = []
        visit = set()
        visit.add(k)
        count = 1
        result = 0
        m[k] = 0
        for d, w in adj_list[k]:
            heapq.heappush(min_heap, (w, k, d))

        while min_heap:
            w, s, d = heapq.heappop(min_heap)

            if d in visit:
                continue

            visit.add(d)
            m[d] = w
            count += 1

            if count == n:
                return m[d]

            for d2, w in adj_list[d]:
                if d2 not in visit:
                    heapq.heappush(min_heap, (m[d] + w, d, d2))
        
        return -1
            