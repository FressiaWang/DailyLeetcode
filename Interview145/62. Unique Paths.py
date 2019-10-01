"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner 
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
**Solution 2 ** (Dynamic Programming)
The recurrance relation between the number of moves at grid (i,j) and previous grids is dp[i-1][j] + dp[i][j-1] 
and a dp matrix is created to memoize the moves at each (i,j).
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*m for _ in range(n)]
        
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]
