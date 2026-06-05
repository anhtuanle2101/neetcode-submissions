'''
    a string s consisting of only uppercase english characters and an integer k
    
    at most k operation, repace any character to a different uppercase english chars

    return longest repeat substring with the replacements
    - 2 nested loop one to be the starting of the substring and inner one to pick the end of the substring
    check if replacements can be done under k operations, if yes, update the max_length
        - check if replacements can be done to convert all charaters into one distinct char under k operations
            - make use of hash map to get the count for each distinct character in the substring, 
            check if sum of all the counts except the largest count equal or less than k meaning we are able
            to replace all the characters into one distinct character substring
    -> O(n^3)

    left, right pointers here, left for the start and right for the end of the substring we are inspecting,
    update the char count at right in the hash map, 
    - check if the sums of all the counts except the max_count <= k, 
        - yes, this means we can make a substring with one character with replacements -> update max_length
        - no, this means we have to move left pointer until we can 
            - before moving left pointer, reduce the char count at left pointer
            - recalculate the min operations to get the desired substring and compare to k 
        
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_length = 0
        char_count = {}
        max_count = 0

        while right < len(s):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            min_operations = (right - left + 1) - max(char_count.values())

            if min_operations <= k:
                max_length = max(max_length, right - left + 1)
                right += 1
                continue
            while min_operations > k:
                char_count[s[left]] -= 1
                left += 1
                min_operations = (right - left + 1) - max(char_count.values())
            
            right += 1
            
        return max_length
            