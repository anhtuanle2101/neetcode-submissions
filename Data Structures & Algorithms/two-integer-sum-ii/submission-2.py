'''
    sorted list nums (non-decreasing)
    one valid solution

    nums[0] is min
    nums[-1] is max

    max_sum -> nums[0] + nums[-1]
    starting from max_sum left=0; right=len(nums)-1, keep checking if the sum compare to the target
    - if the current sum is greater than target
        - current is too big -> move right pointer 
    - elif current sum is smaller than target
        - current sum is too small -> move left pointer
    - 
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        