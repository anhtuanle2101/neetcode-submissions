class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = dict()

        for char in s:
            m[char] = m.get(char, 0) + 1
        
        for char in t:
            if char not in m:
                return False
            m[char] -= 1
            if m[char] == 0:
                del m[char]
        
        return len(m) == 0