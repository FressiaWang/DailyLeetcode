"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            row = [None] * (i + 1)
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(row)
        return ans
