class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = {}
        for x, y in points:
            adj_list[(x, y)] = []

        initial_point = (points[0][0], points[0][1])
        visit = set()
        visit.add(initial_point)
        min_heap = []
        for i in range(1, len(points)):
            d = abs(points[i][0] - initial_point[0]) + abs(points[i][1] - initial_point[1])
            src = initial_point
            dst = (points[i][0], points[i][1])
            heapq.heappush(min_heap, (d, src, dst))
        mst = []
        result = 0
        while min_heap:
            d, src, dst = heapq.heappop(min_heap)

            if dst in visit:
                continue
            mst.append([src, dst])
            result += d

            visit.add(dst)

            src = dst
            for i in range(len(points)):
                dst = (points[i][0], points[i][1])
                if dst not in visit:
                    d = abs(dst[0] - src[0]) + abs(dst[1] - src[1])
                    heapq.heappush(min_heap, (d, src, dst))
        
        return result

        
