class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # arr1 wheere arr1[i] is the product of elements from
        # pos 0 until pos i (forwards, exclusive)
        # if i == 0: arr1[0] = 1
        arr1 = [1] * len(nums)

        for i in range(len(nums)):
            arr1[i] = arr1[i-1] * nums[i-1] if i > 0 else 1

        # arr2 where arr2[i] is the product of elements from
        # the pos len(nums) - 1 until pos i (backwards, exclusive)
        arr2 = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            arr2[i] = arr2[i+1] * nums[i+1] if i < len(nums) - 1 else 1

        results = [1] * len(nums)
        for i in range(len(nums)):
            results[i] = arr1[i] * arr2[i]
        
        return results