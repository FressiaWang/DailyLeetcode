"""
79. Word Search
Medium

2257

114

Favorite

Share
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.search(board,word[1:],r,c):
                        return True
        return False
    def search(self,board,word,r,c):
        if word == '': return True
        tmp=board[r][c]    # it's important for not using the letter twice eg. board[["a","a"]] word "aaa"
        board[r][c]="#"
        if r-1>=0 and board[r-1][c] == word[0]:
            if self.search(board,word[1:],r-1,c):
                return True
        if r+1<=len(board)-1 and board[r+1][c] == word[0]:
            if self.search(board,word[1:],r+1,c):
                return True
        if c-1>=0 and board[r][c-1] == word[0]:
            if self.search(board,word[1:],r,c-1):
                return True
        if c+1<=len(board[0])-1 and board[r][c+1] == word[0]:
            if self.search(board,word[1:],r,c+1):
                return True
        board[r][c]=tmp
        return False
