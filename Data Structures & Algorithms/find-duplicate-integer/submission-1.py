class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # imagine this problem to find the starting point 
        # of a cycle in a linked list
        # for each number in nums, the value at each index
        # will be the next for that node
        # use slow and fast pointers to find the 
        # point where those two pointers meet
        # according to Floyd's algo, the distance
        # from the start of list to start of cycle 
        # equals to distance between the point where two pointers
        # meet to the start of the cycle
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow