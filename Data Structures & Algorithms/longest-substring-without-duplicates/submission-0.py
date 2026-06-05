class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window and data structure set
        # set keep track of unique characters for a substring between pointers l and r
        # so l, r = 0, 0 first off, then r will check the next character
        # if the next character has not existed in the set which means we can add this
        # char into the set update the max_len, then move r to the right by 1
        # otherwise, if the next character existed in the set, 
        # increase l by 1 so there won't be duplicates in the substring
        # until r < len(s)

        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        st = set()
        st.add(s[l])
        max_len = 1
        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                max_len = max(max_len, len(st))
                r += 1
            else:
                st.remove(s[l])
                l += 1
        
        return max_len