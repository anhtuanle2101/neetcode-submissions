class Solution:
    def climbStairs(self, n: int) -> int:
        rs = [0] * (n + 1)

        rs[0] = 1
        rs[1] = 1

        if n < 2:
            return rs[n]

        for i in range(2, n+1):
            rs[i] = rs[i-1] + rs[i-2]
        
        return rs[n]