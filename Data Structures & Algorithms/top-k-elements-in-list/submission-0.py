'''
    Given an integer array nums and an integer k
    => return k elements where those are the most frequent in nums
    - [1,2,2,3,3,3] => most frequent is 3, 2 and lastly 1, k = 2 means return 2 numbers with the most frequent count, where are 3 and 2
    - Get the distinct number count -> use a hash map with key being the distinct number and update the value count by one each time we see
    the number
    - zip the hash map (number->count) into (count, number) values and heapify the array into a max heap
        - to return k largest count value pairs k * log n whereas to sort the value pairs of count and distinct number would be n * log n 

    Answer is unique and order not matters
    - nums can be neg
    - k: [1, len(distinct_num)]
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_count = {}

        # frequent count each distinct number in nums
        for num in nums:
            if num in frequent_count:
                frequent_count[num] += 1
                continue

            frequent_count[num] = 1

        # zip the hash map pairs into an array of (count, number) pairs
        max_heap = [(-count, number) for number, count in frequent_count.items()]
        heapq.heapify(max_heap)

        result = []
        for i in range(k):
            largest_count, number = heapq.heappop(max_heap)
            result.append(number)
        
        return result
        
        
