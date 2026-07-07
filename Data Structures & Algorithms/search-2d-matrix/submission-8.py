class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 0 to m*n
        # m rows 
        # n columns 
        # num // columns
        # num mod columns 

        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])

        l, r  = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2

            idx_row, idx_col = mid // n, mid % n
            if matrix[idx_row][idx_col] > target:
                r = mid - 1
            elif matrix[idx_row][idx_col] < target:
                l = mid + 1
            else:
                return True
            
        return False