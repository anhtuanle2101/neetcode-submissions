class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]*len(nums)
        postfix_products = [1]*len(nums)

        for i in range(len(nums)):
            prefix_products[i] = (prefix_products[i-1] if i - 1 in range(len(nums)) else 1) * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            postfix_products[i] = (postfix_products[i+1] if i+1 in range(len(nums)) else 1)*nums[i]
       
        results = [1]*len(nums)

        for i in range(len(nums)):
            results[i] = (prefix_products[i-1] if i-1 in range(len(nums)) else 1)*(postfix_products[i+1] if i+1 in range(len(nums)) else 1)

        return results