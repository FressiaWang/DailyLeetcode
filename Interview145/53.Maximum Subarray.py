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

def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
 
def max_sum(nums):
    ret = float("-inf")  # 负无穷
    if not nums:
        return ret
    current = 0
    for i in nums:
        if current <= 0:
            current = i
        else:
            current += i
        ret = max(ret, current)
    return ret

# DP, constant space
def maxSubArray2(self, nums):
    if not nums:
        return None
    loc = glo= nums[0]
    for i in xrange(1, len(nums)):
        loc = max(loc+nums[i], nums[i])
        glo = max(loc, glo)
    return glo

def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) / 2
        
        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)
        
        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)
            
        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)
            
        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))
        
     def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
