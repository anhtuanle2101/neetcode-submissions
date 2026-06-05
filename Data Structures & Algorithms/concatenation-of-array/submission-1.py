class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))

        for i in range(2):
            for j in range(len(nums)):
                ans[i*len(nums) + j] = nums[j]
        
        return ans

        # O(n) space
        # O(n) time