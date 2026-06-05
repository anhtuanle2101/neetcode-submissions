class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.cur = []

        self.s = s

        self.dfs(0)

        return self.result

    def dfs(self, i):
        if i == len(self.s):
            self.result.append(self.cur[:])
            return

        for j in range(i, len(self.s)):
            if not self.isPalindrome(self.s[i: j+1]):
                continue
            self.cur.append(self.s[i: j+1])
            self.dfs(j + 1)
            self.cur.pop()

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True