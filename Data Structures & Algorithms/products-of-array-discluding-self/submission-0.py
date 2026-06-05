"""
    nums = int array
    output = int array where output[i] = product all elements except nums[i]

    prefix_product = int array where prefix_product[i] is the product of elements starting from 0th to (i-1)th
    prefix_product[0] = 1
    postfix_product = int array where postfix_product[i] is the product of elements starting from len(nums)-1th to (i+1)th
    postfix_product[len(nums) - 1] = 1
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            prefix[i] *= postfix[i]

        return prefix