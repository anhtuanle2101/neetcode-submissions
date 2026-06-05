class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.cur = []
        self.nums = nums
        self.nums.sort()

        self.dfs(0)
    
        return self.result

    def dfs(self, i):
        if i == len(self.nums):
            self.result.append(self.cur[:])
            return
        self.cur.append(self.nums[i])

        self.dfs(i + 1)

        self.cur.pop()

        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i + 1]:
            i = i + 1
        
        self.dfs(i + 1)
        