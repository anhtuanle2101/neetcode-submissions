'''
    length of the longest substring without duplicate characters
    - set to detect duplicate

    naive approach here we could have 2 nested loop one outer loop for the first char of the substring
    and second loop of the ending of the substring, 
    check if the substring has no duplicates, if yes, update the max_lengh -> O(n^2)
    - use a set to check duplicate 
    for c in substring:
        if c in s:
            duplicates = True
        s.add(c)

    if duplicates:
        continue
    
    max_length = max(max_length, len(substring))
    abc
    a
    ab
    abc -> max length substring -> return 3
    b
    bc
    c
    
    2 pointers left, right the substring will be presented as substring = s[left:right+1], so now if we are
    moving right by one each time, 
    - if char at right pointer not exist in the set -> no duplicate -> add it to the set 
        - update the max_length
    - else the char at right pointer existed in the set -> this is a duplicate and we do not want this
        - set the left to where right point to 
        - reset the set
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_length = 0

        left, right = 0, 0
        no_duplicates = set()
        # substring = s[left: right+1]
        while right < len(s):
            if s[right] not in no_duplicates:
                no_duplicates.add(s[right])
                max_length = max(max_length, len(no_duplicates))
                right += 1
                continue
            
            while s[right] in no_duplicates:
                no_duplicates.remove(s[left])
                left += 1
        
        return max_length
    
