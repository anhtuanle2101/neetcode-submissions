'''
    sorted and rotated ints 

    find the min element

    the ints can be seperated into two parts left (second half of original ints) and right (first half of original)
    we can take the middle element
    - identify the middle element is in the left or right part
        - if the middle is in the right part, take another look at left side 
        - else, take a look at the other half (right)
    - to identify if the middle is in the left or right part
        - nums[middle] > last_num -> middle is in the left part -> take a look right of middle
        - nums[middle] < last_num -> middle is in the right part -> take a look at left of middle
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, last = 0, len(nums) - 1, len(nums) - 1

        while left <= right:
            middle = left + (right-left)//2

            if nums[middle] > nums[last]:
                left = middle + 1
            elif nums[middle] <= nums[last]:
                right = middle - 1
        
        return nums[left]