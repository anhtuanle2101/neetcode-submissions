class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        rows_check = [set() for i in range(rows)] 
        cols_check = [set() for i in range(cols)] 
        boxes_check = [set() for i in range(rows//3 * cols//3)]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in rows_check[i]:
                    print(board[i][j])
                    print(rows_check[i])
                    return False
                if board[i][j] in cols_check[j]:
                    return False
                if board[i][j] in boxes_check[(i//3)*3+(j//3)]:
                    return False
                rows_check[i].add(board[i][j])
                cols_check[j].add(board[i][j])
                boxes_check[(i//3)*3+j//3].add(board[i][j])

        return True