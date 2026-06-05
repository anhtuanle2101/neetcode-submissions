class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - 65] += 1
        
        max_heap = [(-f, chr(i + 65)) for i,f in enumerate(freq) if f > 0]
        print(max_heap)
        heapq.heapify(max_heap)

        m = {}
        i = 0
        while True:
            if len(max_heap) > 0:
                f, c = heapq.heappop(max_heap)
                f = -f - 1
                # get the most frequent character from heap
                # subtract freq by 1, if it is larger than 0 we have to 
                # save it state (f, c) to its next available index
                if f > 0:
                    m[c] = (f, i+n)
            
            # check in m if there is any character available to put it back to the heap
            # delete
            delete = []
            for c in m:
                if m[c][1] == i:
                    heapq.heappush(max_heap, (-m[c][0], c))
                    delete.append(c)
            
            for d in delete:
                del m[d]

            i += 1
            if len(m) == 0 and len(max_heap) == 0:
                break

        return i

