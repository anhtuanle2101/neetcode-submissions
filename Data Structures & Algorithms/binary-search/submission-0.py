class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            cur = nums[mid]

            if cur > target:
                r = mid - 1
            elif cur < target:
                l = mid + 1
            else:
                return mid
        
        return -1