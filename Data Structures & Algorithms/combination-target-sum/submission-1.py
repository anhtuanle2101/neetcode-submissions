'''
    unique ints and target
    unique subsets where sum(subsets) = target
    same int came be chosen multiple times (inf)
    - at ith num, there are number of distinct options
        - check if current total == target
            - if yes, this is a valid subset -> add to the result
        
        - add ith num to the current list and current total then move to ith
        - back track
        - not include ith num and move to i + 1th
'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []

        def backtrack(i, cur_total):
            if cur_total == target:
                result.append(cur[:])
                return
            if i == len(nums) or cur_total > target:
                return

            
            cur.append(nums[i])
            cur_total += nums[i]
            # move forward
            backtrack(i, cur_total)
            # backtrack
            cur.pop()
            cur_total -= nums[i]
            
            # not include nums[i] and move forward
            backtrack(i + 1, cur_total)

        backtrack(0, 0)

        return result

                
                    
