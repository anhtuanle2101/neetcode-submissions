class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.cur = []
        self.nums = nums
        self.dfs(0)

        return self.result

    def dfs(self, i):
        if i == len(self.nums):
            self.result.append(self.cur[:])
            return
        
        for idx in range(len(self.cur) + 1):
            self.cur.insert(idx, self.nums[i])
            self.dfs(i + 1)

            self.cur.remove(self.nums[i])
