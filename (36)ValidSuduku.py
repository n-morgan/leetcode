"""

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row_dict = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row = int(i)
                elt = int(board[i][j])
                if row not in row_dict:
                    row_dict[row] = set()
                if elt in row_dict[row]:
                    return False
                row_dict[row].add(elt)

        col_dict = {}
        for j in range(9):
            for i in range(9):
                if board[i][j] == ".":
                    continue

                col = int(j)
                elt = int(board[i][j])
                if col not in col_dict:
                    col_dict[col] = set()
                if elt in col_dict[col]:
                    return False
                col_dict[col].add(elt)
        
        sub_dict = {}
        for i in (0,3,6):
            
            for row in range(i, i+3):
                for j in (0,3,6):
                    for col in range(j, j+3):
                        if board[row][col] == ".":
                            continue
                        elt = int(board[row][col])
                        if (i,j) not in sub_dict:
                            sub_dict[(i,j)] = set()
                        if elt in sub_dict[(i,j)]:
                            return False
                        sub_dict[(i,j)].add(elt)
                        
                
        return True


if __name__ == "__main__":
    solver = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(solver.isValidSudoku(board))
