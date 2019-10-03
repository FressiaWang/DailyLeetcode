"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = set(nums)
        res = [[]]
        for n in nums:
            for i in range(len(res)):    # for s in res: doesn't work because res update immediately to make the loop infinitely 
                res.append(res[i]+[n])   # res.append(s + [n])
        return res
