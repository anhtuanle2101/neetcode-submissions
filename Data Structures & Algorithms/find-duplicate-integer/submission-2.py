'''You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.
- array n + 1 ints ~ len(nums) = n + 1
- nums[i]: [1, n], each int appear once except one -> return this int

Can you solve the problem without modifying the array nums and using O(1) extra space?
- can be solved using set -> O(n) space
    - iterate through nums, for each num check if the num exists, if yes, return the num, else put it in the set
- so for each unique num in nums, there should be only one relation pointing from index i to nums[i]
    - since the ints bound are [1, n], they are sequential and can form a linked list 
    - duplicated num will be the start of the cycle in the linked list since there will be pointers point to this node 
    - since the distance from the start to the start of the cycle equals distance from the fast and slow pointers meet to the start of the cycle 
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while slow != fast or slow == 0:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow_and_fast_intersection, linked_list_head = slow, 0

        while slow_and_fast_intersection != linked_list_head:
            slow_and_fast_intersection = nums[slow_and_fast_intersection]
            linked_list_head = nums[linked_list_head]
        
        return slow_and_fast_intersection