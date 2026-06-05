class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.cur = []

        self.nums = candidates
        self.nums.sort()

        self.target = target

        print(self.nums)

        self.dfs(0)

        return self.result

    def dfs(self, i):
        if sum(self.cur) == self.target:
            self.result.append(self.cur[:])
            return

        if i >= len(self.nums):
            return
        
        self.cur.append(self.nums[i])

        self.dfs(i + 1)

        self.cur.pop()

        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i + 1]:
            i += 1

        self.dfs(i + 1)