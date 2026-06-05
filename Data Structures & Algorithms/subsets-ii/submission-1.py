'''
    nums: ints 
    - possible duplicates
        - sort?
    - return no duplicate subsets 
    - order no matter

    at ith int with sorted ints 
        - there distinct options
            - choose int at ith be a part of the subset
            - not to choose the int at ith -> shift
    
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.cur = []
        self.nums = nums
        self.nums.sort()

        self.backtrack(0)

        return self.result

    def backtrack(self, i):
        if i == len(self.nums):
            self.result.append(self.cur[:])
            return
        
        self.cur.append(self.nums[i])

        self.backtrack(i + 1)
        self.cur.pop()

        # not include the nums[i] part of subset
        while i + 1 < len(self.nums) and self.nums[i] == self.nums[i + 1]:
            i += 1

        self.backtrack(i + 1)
