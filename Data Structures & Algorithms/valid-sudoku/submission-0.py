'''
    rules:
    - each row have no duplicates -> 9 rows
    - each col have no dupicates -> 9 cols
    - each 3 by 3 subsquare have no duplicates -> 9 subboxes
        - use set to detect duplication for each validation
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = len(board)

        for i in range(rows):
            # check duplicates in cols
            unique_nums = set()

            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if board[i][j] in unique_nums:
                    return False
                unique_nums.add(board[i][j])
            
            #check duplicates in rows
            unique_nums = set()
            for j in range(cols):
                if board[j][i] == ".":
                    continue
                if board[j][i] in unique_nums:
                    return False
                unique_nums.add(board[j][i])

            # check duplicates in ith subbox
            unique_nums = set()
            # for the ith subbox, the rows be [i//3, i//3 + 2] [i%3, i%3 + 2]
            for r in range(i//3 * 3, i//3 * 3 + 3):
                for c in range(i%3 * 3, i%3 * 3 + 3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in unique_nums:
                        return False
                    unique_nums.add(board[r][c])

        return True        