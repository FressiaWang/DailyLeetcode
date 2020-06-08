"""
53. Maximum Subarray
Easy

5142

199

Favorite

Share
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution 
using the divide and conquer approach, which is more subtle.

Dynamic programming
"""
class Solution(object):
def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    import sys
    pre, MAX_SUM=0,-sys.maxint-1 #mm:the sum before nums[i],MAX_SUM:maxest sum of subarray
    start,end=0,0 #record the sign of subarray
    for i in xrange(len(nums)):
    #whether the sum before nums[i] is smaller than 0, if it's, throw away(becuase add a negative 
    #will get smaller and start from the nums[i];else add it to nums[i]
        if pre>0:)
            pre += nums[i]
        else:
            pre = nums[i]
            start=i
        if pre > MAX_SUM:
            MAX_SUM = pre
            end=i
    return MAX_SUM
