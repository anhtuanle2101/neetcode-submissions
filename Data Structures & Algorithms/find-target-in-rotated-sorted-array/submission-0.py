class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # binary search

        while l <= r:
            #get mid element
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]:
                # left portion
                if nums[mid] < target or target < nums[l]:
                    # target is in right portion or found element is too small
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # right portion
                if target >= nums[l] or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1