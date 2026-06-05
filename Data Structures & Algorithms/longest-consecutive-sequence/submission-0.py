'''
    Return the length of the longest consecutive sequence of elements.
    - i + 1th element is 1 greater than ith element ith, i+1th are both in consecutive sequence

    - O(n) time constraint -> no sorting 
        - hash_map to count the longest consecutive character has so far
        - at next character ith, check if check if nums[i] + 1 or nums[i] - 1 exists in the hash map,
        if yes update the consecutive count for each valid comparison and add this to the hash_map
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        result = 0

        for i in range(len(nums)):
            if nums[i] in s:
                continue

            s.add(nums[i])
        
        for num in list(s):
            if num - 1 in s:
                continue
            
            count = 1
            while num + count in s:
                count += 1
            
            result = max(result, count)
    
        return result
                

                