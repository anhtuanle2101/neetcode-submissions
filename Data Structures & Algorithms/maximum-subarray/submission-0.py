'''
    nums int[]
    find largest sum of subarray from nums 

    - iterate through num in nums
        - keep track current max sum of subarrays ending at num 
            - if the max sum ending before num is negative -> ignore that sum and set current max sum is num 
            - keep update the max sum result 
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = nums[0]

        cur_max = 0

        for i in range(len(nums)):
            if cur_max < 0:
                cur_max = 0
            cur_max += nums[i]
            max_res = max(max_res, cur_max)

        return max_res