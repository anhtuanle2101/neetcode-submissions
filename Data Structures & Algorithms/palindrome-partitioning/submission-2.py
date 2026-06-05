'''
    s string
    OUT: split into substrings where each substring is palindrome, return list of all posibble substrings
    - order not matter

    - for n characters -> we can split at most n spots
        - for ith split
            
            - loop through rest of the string j [i: len(s)]
                - check if substring [i:j+1] is palindrome
                    - if not, stop going deeper
                - moving forward with splitting next substring starting at j + 1
                - backtrack
            
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.cur = []
        self.s = s

        self.backtrack(0)

        return self.result

    def backtrack(self, i):
        if i >= len(self.s):
            self.result.append(self.cur[:])
            return
        def is_palindrome(l, r):
            while l < r:
                if self.s[l] != self.s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        for j in range(i, len(self.s)):
            if not is_palindrome(i, j):
                continue
            
            self.cur.append(self.s[i:j+1])
            print(self.cur)
            # move forward
            self.backtrack(j + 1)
            self.cur.pop()

        
        
        