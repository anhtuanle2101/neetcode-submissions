class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
        
    def binarySearch(self, nums, s, e, target):
        if e - s + 1 < 1:
            return -1

        mid = (s + e) // 2

        if nums[mid] > target:
            return self.binarySearch(nums, s, mid - 1, target)
        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, e, target)
        else:
            return mid
