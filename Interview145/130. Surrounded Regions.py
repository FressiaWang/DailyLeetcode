"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return board
        r, c = len(board), len(board[0])
        adjent = collections.deque()
        for i in range(r):
            adjent += [(i,0),(i,c-1)]

        for j in range(c):
            adjent += [(0,j),(r-1,j)]
        """
        for i in range(r):
            for j in range(c):
                if (i in [0, r-1] or j in [0, c-1]) and board[i][j] == 'O':
                    adjent.append((i,j))
        """
        while adjent:
            i, j = adjent.popleft()
            if 0<=i<r and 0<=j<c and board[i][j] == 'O':
                board[i][j] = 'N'
                adjent += [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'N':
                    board[i][j] = 'O'
