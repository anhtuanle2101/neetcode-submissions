'''
    unique ints
    permutations
    order not matter
    - at ith num, we have list of permutations from 0 to i-1th -> len(each_perm) = i -> there are i + 1 spots ith can fit into 
        - if i == len(nums)
            - we have a valid permutation -> append to result
        - for permutation in cur result list
            - for each available spot
                - put ith num into the spot
                - move forward to next i + 1 num
                - backtrack
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.cur = [[]]
        self.nums = nums

        self.backtrack(0)

        return self.cur

       

    def backtrack(self, i):
        if i == len(self.nums):
            return
        
        temp_perms = []
        for k in range(len(self.cur)):
            for j in range(len(self.cur[k]) + 1):
                copy = self.cur[k][:]
                copy.insert(j, self.nums[i])
                temp_perms.append(copy)
        self.cur = temp_perms
        # move forward 
        self.backtrack(i + 1)
                