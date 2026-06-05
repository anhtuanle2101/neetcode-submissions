class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums list O(nlogn)
        # loop through each element 
        # from i + 1 till the end of nums
        # find two sums equals to -nums[i]
        
        nums.sort()
        st = set()
        results = []

        for i in range(len(nums)):
            cur_num = nums[i]
            target = -cur_num
            s, e = i + 1, len(nums) - 1
            while s < e:
                two_sum = nums[s] + nums[e]
                if two_sum > target:
                    e -= 1
                elif two_sum < target:
                    s += 1
                else:
                    if tuple([cur_num, nums[s], nums[e]]) in st:
                        s += 1
                        continue
                    results.append([cur_num, nums[s], nums[e]])
                    st.add(tuple([cur_num, nums[s], nums[e]]))
                    s += 1
            
        return results
                    
            
        

