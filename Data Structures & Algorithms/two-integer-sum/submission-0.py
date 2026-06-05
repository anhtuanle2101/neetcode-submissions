class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            cur = nums[i]

            if (target - cur) in hash_map:
                return [hash_map[target - cur], i]

            if cur not in hash_map:
                hash_map[cur] = i