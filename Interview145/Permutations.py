"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(remain, stack):
            if remain == []:
                res.append(stack)
            for i in range(len(remain)):
                r = copy.copy(remain)
                n = r.pop(i)

                dfs(r, stack + [n])

        dfs(nums, [])
        return res
