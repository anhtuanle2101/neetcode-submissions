class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # sliding window
        # l, r being a window of a substring of size len(s1) in s2
        # calculate frequency of each character of the substring 
        # until r - l + 1 == len(s1) so that we have two equal 
        # size substring to check if they are permutation
        # if they are, return true
        # otherwise, move r and l by 1, and update frequency of s[r] by 1 increase, and 
        # s[l] by 1 decrease 
        m_s1 = dict()
        for i in range(len(s1)):
            m_s1[s1[i]] = m_s1.get(s1[i], 0) + 1
        l, r = 0, 0
        m = dict()
        while r < len(s2):
            m[s2[r]] = m.get(s2[r], 0) + 1
            if r - l + 1 < len(s1):
                r += 1
                continue
            
            # compare
            is_permutation = True
            for k in m_s1.keys():
                if m.get(k, 0) != m_s1.get(k, 0):
                    is_permutation = False
                    break
            if is_permutation is True:
                return True
            else:
                m[s2[l]] -= 1
                l += 1
                r += 1
        
        return False
