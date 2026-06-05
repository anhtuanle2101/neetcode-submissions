class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total_w = 0
        max_left, max_right = 0, 0

        while l <= r:
            if max_left <= max_right:
                w = max_left - height[l]
                if height[l] > max_left:
                    max_left = height[l]
                if w > 0:
                    total_w += w
                l += 1
            else:
                w = max_right - height[r]
                if height[r] > max_right:
                    max_right = height[r]
                if w > 0:
                    total_w += w
                r -= 1
        
        return total_w