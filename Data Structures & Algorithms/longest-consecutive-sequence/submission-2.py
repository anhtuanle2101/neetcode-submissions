class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
        for num in m:
            tmp = num
            while tmp - 1 in m:
                m[num] += 1
                tmp -= 1
        
        return max(list(m.values()))