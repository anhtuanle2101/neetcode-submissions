class Solution:
    def trap(self, height: List[int]) -> int:
        # Make use of two pointers, 
        # and keeping track of the max value on the left of the left pointer
        # and the max value on the right of the right pointer
        # At each iteration, since we are looking for the min(maxL, maxR)
        # if maxL is smaller or equal to maxR, we will calculate the 
        # water can be contained at the left pointer
        # otherwise, calculate the water can be contained at the right pointer
        # to calculate the water can be contained, 
        # since at left pointer, we know maxL was the bottleneck, similar to at right pointer
        # then w = maxL - h[l_pointer] or at right pointer w = maxR - h[r_pointer]
        # then according update maxL and maxR 

        l, r = 0, len(height) - 1
        water = 0
        maxL, maxR = 0, 0
        while l <= r:
            if maxL <= maxR:
                w = maxL - height[l]
                if w > 0:
                    water += w
                if height[l] > maxL:
                    maxL = height[l]
                l += 1
            else:
                w = maxR - height[r]
                if w > 0:
                    water += w
                if height[r] > maxR:
                    maxR = height[r]
                r -= 1
        
        return water