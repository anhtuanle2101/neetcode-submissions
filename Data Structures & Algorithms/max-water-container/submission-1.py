'''
    water contained = min(left_bar, right_bar) * distance
    - to maximum the water contained
        -> max(distance) -> starting left at start and right at the end
        -> to increase the min(left_bar, right_bar), we only move the bar which value is smaller
        -> keep doing this until two pointers are crossed, at each iteration, check against max

'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left, right = 0, len(heights) - 1

        while left < right:
            water = min(heights[left], heights[right]) * (right - left)

            res = max(res, water)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return res