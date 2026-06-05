class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = l + (r - l) // 2
            print(mid)

            cur = matrix[mid // cols][mid % cols]
            if cur > target:
                r = mid - 1
            elif cur < target:
                l = mid + 1
            else:
                return True

        return False