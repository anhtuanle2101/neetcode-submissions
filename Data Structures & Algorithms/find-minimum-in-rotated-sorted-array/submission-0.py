class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1 
        rs = math.inf
        while l <= r:
            if nums[l] < nums[r]:
                return min(rs, nums[l])
            mid = l + (r - l)//2
        
            rs = min(rs, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return rs