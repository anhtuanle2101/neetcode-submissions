class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack
        # storing the index as the ealiest index that 
        # the height can extends back
        
        max_area = 0

        stack = []

        for i, h in enumerate(heights):
            # (3, 2)
            # if stack is empty add it to the stack
            if not stack:
                stack.append((i, h))
                continue
            
            if h > max_area:
                max_area = h

            # if the current height is less than 
            # the last height in stack,
            # the last height cannot extends to the right
            ix = i # 3
            if h < stack[-1][1]:     
                while stack and stack[-1][1] >= h:
                    (ix, hx) = stack.pop() 
                    area = hx * (i - ix) 
                    if area > max_area:
                        max_area = area 
            stack.append((ix, h))
        print(stack)
        last_idx = len(heights) - 1
        while stack:
            i, h = stack.pop()
            area = (last_idx - i + 1) * h 
            if area > max_area:
                max_area = area
            
        return max_area

        


        