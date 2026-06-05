'''
    binary search
    rows, cols = len(matrix), len(matrix[0])
    i: [0, rows * cols]
    current_row = i // rows
    current_cols = i // cols * cols + i % cols
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2

            current_row, current_col = middle // cols, middle % cols
            
            middle_value = matrix[current_row][current_col]

            if middle_value == target:
                return True
            elif middle_value < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False