class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # there is the data structure which is very efficient in 
        # detecting duplicate (set)
        # since set only store unique number
        # so for each number in the input array, check if the number exists in the set yet,
        # if yes, return True,
        # else, add the number into the set making sure if the duplicate number appear later in the array 
        # will be detected
        # if the there is no duplicate found after going through the numbers
        # then there is no duplicates, return False

        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)

        return False