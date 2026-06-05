class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.cur = []
        self.nums = nums
    
        self.dfs(0)

        return self.result
        
    def dfs(self, i):
        if i == len(self.nums):
            self.result.append(self.cur.copy())
            return
        
        self.cur.append(self.nums[i])
        self.dfs(i + 1)
        self.cur.pop()
        self.dfs(i + 1)
    
