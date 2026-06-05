class Solution:
    def climbStairs(self, n: int) -> int:
        rs = [0] * n

        if n <= 1:
            return 1

        rs[0] = 1
        rs[1] = 2

        for i in range(2, n):
            rs[i] = rs[i-1] + rs[i-2]
        
        return rs[n - 1]