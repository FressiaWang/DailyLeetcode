"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board))
    
    def isValidUnit(self, unit):
        unit = [i for i in unit if i!= '.']
        return len(unit) == len(set(unit))
    
    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True
    
    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        return True
    
    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j, j+3)]
                if not self.isValidUnit(square):
                    return False
        return True
        
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    big = set()
    for i in range(9):
        for j in range(9):
            if board[i][j]!='.':
                cur = board[i][j]
                if (i,cur) in big or (cur,j) in big or (i//3,j//3,cur) in big:
                    return False
                big.add((i,cur))
                big.add((cur,j))
                big.add((i//3,j//3,cur))
    return True
