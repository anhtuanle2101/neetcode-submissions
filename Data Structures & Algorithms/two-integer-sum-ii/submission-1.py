class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Make use of two pointers 
        # one at the end and one at the start of the array
        # we know that the left pointer will be the smallest element
        # the right pointer will be the largest element
        # if take a sum of those two pointers and compare it 
        # to the target, if the sum is too small, which means,
        # we should move the left pointer to the right by one to
        # increase the sum, otherwise, if the sum is too large compared
        # to target, we move the right pointer to the left by 1
        # We loop until l == r, but we assumes there will be
        # exactly one valid solution which we do not have 
        # to handle case where there are no two pointers sum up to 
        # the target
        l, r = 0, len(numbers)-1

        while l < r:
            cur_sum = numbers[l] + numbers[r]
    
            if cur_sum < target: # too small
                l += 1
            elif cur_sum > target: # too large
                r -= 1
            else:
                return [l + 1, r + 1]