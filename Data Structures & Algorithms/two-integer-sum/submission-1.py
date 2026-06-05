class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of a dict of unique numbers to its position that we checked, 
        # at next number, check if the (target - number) exists in the set which
        # we have checked it in the past and put it here,
        # we can return the result (dict[target-cur_num], cur_idx)

        d = {}

        for idx, num in enumerate(nums):
            if target - num in d:
                return [d[target-num], idx]

            d[num] = idx

        
        