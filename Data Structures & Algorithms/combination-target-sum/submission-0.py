class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.total = 0
        self.target = target
        
        self.result = []
        self.cur = []

        self.dfs(0, nums)

        return self.result
        
    def dfs(self, i, nums):
        if self.total == self.target:
            self.result.append(self.cur.copy())
            return

        if i >= len(nums) or self.total > self.target:
            return

        self.cur.append(nums[i])
        self.total += nums[i]

        self.dfs(i, nums)

        self.cur.pop()
        self.total -= nums[i]

        self.dfs(i + 1, nums)