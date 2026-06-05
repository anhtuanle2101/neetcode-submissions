'''
    unique ints nums
    no duplicate subsets
    order not matter
    - at ith num, there are 2 distinct options 
        - pick ith num
            - moving forward to the next i + 1th num
        - don't pick ith num
            - moving forward to the next i + 1th num
        - stopping condition, if i is out of range (i == len(nums))
            - this is a valid subset (no duplicate since at each step we chose distinct path)
                - put the subset into the result
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []

        def backtrack(i):
            if i == len(nums):
                result.append(cur[:])
                return

            # pick ith num
            cur.append(nums[i])
            # move forward
            backtrack(i + 1)
            # backtrack
            cur.pop()

            # don't pick ith num and move forward
            backtrack(i + 1)
            
        backtrack(0)
        
        return result