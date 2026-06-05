class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)

        return len(set(nums)) != len_nums