class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        # l,r being two pointers represent substring in s
        # we want to find shortest substring 
        # use of two hash maps to store count of unique characters of t in t and s
        # make use of two variables called need_count for number of unique characters
        # needed in t, and have_count for number of unique characters sastify the 
        # condition in t 
        # r go through each character in s if s[r] exists in t hash map, 
        # increment s hash map at s[r] by 1
        # check against the condition, if sastify, 
        # increment have by 1, then check if have_count equals to need_count
        # if yes, calculate the distance between l and r and update min_len accordingly
        #   after that, remove s[l] one by one until the condition is not sastified 
        #   any more, checking the distance between l and r and update min_len accordingly
        # otherwise, continue
        #
        if len(s) < len(t):
            return "" 
        m_t, m_s = dict(), dict()
        need_count, have_count = 0, 0
        for i in range(len(t)):
            m_t[t[i]] = m_t.get(t[i], 0) + 1
        need_count = len(m_t)
        min_range = [0, len(s) - 1]
        check = False
        l, r = 0, 0
        while r < len(s):
            next_character = s[r]
            if next_character not in m_t:
                r += 1
                continue
            m_s[next_character] = m_s.get(next_character, 0) + 1
            if m_s[next_character] == m_t[next_character]: # condition
                have_count += 1

            if have_count == need_count:
                check = True
                distance = r - l + 1
                min_distance = min_range[1] - min_range[0] + 1
                if distance < min_distance:
                    min_range = [l, r]
                
                while have_count == need_count:
                    start_character = s[l]
                    if start_character in m_t:
                        m_s[start_character] -= 1
                        if m_s[start_character] < m_t[start_character]:
                            have_count -= 1
                            l += 1
                            continue
                    l += 1 
                    distance = r - l + 1
                    min_distance = min_range[1] - min_range[0] + 1
                    min_range = [l, r] if distance < min_distance else min_range
            r += 1
        
        return s[min_range[0]: min_range[1] + 1] if check else ""
                




            

        