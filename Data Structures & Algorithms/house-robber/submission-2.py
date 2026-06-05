class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        two = nums[0]
        one = max(two, nums[1])

        for i in range(2, len(nums)):
            cur = max(two + nums[i], one)
            two = one
            one = cur
        
        return max(one, two)