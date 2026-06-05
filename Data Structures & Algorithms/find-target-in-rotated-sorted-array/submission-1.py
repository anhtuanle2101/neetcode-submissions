'''
    sorted and rotated ints 

    target

    return the index if target is found, else -1

    for a ith element,
    nums[middle] <= nums[last] -> right part
    -   middle is in the right part
        if target is also in right part? 
            - if nums[middle] > target ? target is on the left of middle
            - else nums[middle] < target ? target is on the right of middle 
        if target is on the left part -> look to the left of middle
    nums[middle] >= nums[last] -> left part
        if target is on the same part
            - if nums[middle] > target ? target is on the left of middle
            - else nums[middle] < target ? target is on the right of middle 
        else:
            look to the right of middle
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, last = 0, len(nums)-1 , -1

        while left <= right:
            middle = left + (right-left)//2

            if nums[middle] == target:
                return middle
            # middle is in right
            if nums[middle] <= nums[last]:
                if nums[middle] > target or target > nums[last]:
                    right = middle - 1
                else:
                    left = middle + 1
            # middle is in left
            else:
                if nums[middle] < target or target <= nums[last]:
                    left = middle + 1
                else:
                    right = middle - 1
                

        return -1