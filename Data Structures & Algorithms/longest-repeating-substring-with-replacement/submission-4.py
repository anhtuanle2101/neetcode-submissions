class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window with dynamic array
        # the array will be a array of 26 elements representing frequency
        # of the uppercase english characters in s
        # two pointers l, r represent window of a substring from s
        # until r < len(s)
        # calculate min number of replacements need to be made 
        # to convert the substring into a substring contains only one distinct character
        # if this number of replacements is less or equal to k, it is valid
        # update the max_len accordingly
        # and increase r by 1
        # otherwise, move l pointer by 1 to reduce number of replacements

        if len(s) < 2:
            return len(s)
        arr = [0] * 26
        l, r = 0, 1
        max_len = 1
        arr[ord(s[l]) - 65] += 1
        arr[ord(s[r]) - 65] += 1
        while r < len(s):
            min_replace = (r - l + 1) - max(arr)
            if max(arr) != r - l + 1 and min_replace > k:
                arr[ord(s[l]) - 65] -= 1
                l += 1
                continue
            max_len = max(max_len, r - l + 1)
            r += 1
            if r < len(s):
                arr[ord(s[r]) - 65] += 1
        
        return max_len