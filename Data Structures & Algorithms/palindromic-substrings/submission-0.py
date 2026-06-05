class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # odd palindromes

        for c in range(len(s)):
            l, r = c, c
            count += 1
            while l - 1 in range(len(s)) and r + 1 in range(len(s)) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
                count += 1
        
        # even palindromes
        for c in range(len(s) - 1):
            l, r  = c, c + 1
            if s[l] == s[r]:
                count += 1
                while l - 1 in range(len(s)) and r + 1 in range(len(s)) and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                    count += 1
        
        return count