class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap respect to distance of each point to the origin
        # for each point, calculate the corresponding distance from that point to the origin
        # zip (distance, point) and heapify this array into a min heap
        # to return k closest points which means return k points of whose distance are smallest
        # iterate k times, each time pop from the min heap append the point to the result array
        # return the result array

        result = []
        min_heap = [(self.calculate_distance(point), point) for point in points]
        heapq.heapify(min_heap)

        for i in range(k):
            if not min_heap:
                break
            result.append(heapq.heappop(min_heap)[1])
        
        return result

    def calculate_distance(self, point):
        x, y = point

        return pow(x, 2) + pow(y, 2)