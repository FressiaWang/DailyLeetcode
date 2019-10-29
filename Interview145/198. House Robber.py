"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.
"""
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        # DP O(n) time, O(1) space
        # ik: max include house k
        # ek: max exclude house k, (Note: ek is also the maximum for house 1,...,k-1)
        # i[k+1]: num[k] + ek #can't include house k
        # e[k+1]: max(ik, ek) # can either include house k or exclude house k
        i, e = 0, 0
        for n in num: #from k-1 to k
            i, e = n+e, max(i,e)
        return max(i,e)

class Solution:
# @param {integer[]} nums
# @return {integer}
def rob(self, nums):
    l = r = 0
    for n in nums:
        l, r = r, max(n + l, r)
    return r
    
 class Solution:
        # @param num, a list of integer
        # @return an integer
        def rob(self, num):
            max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
            for cur in num:
                max_3_house_before, max_2_house_before, adjacent = \
                max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
            return max(max_2_house_before, adjacent)
# O(n) space
def rob1(self, nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    res = [0] * len(nums)
    res[0], res[1] = nums[0], max(nums[0], nums[1])
    for i in xrange(2, len(nums)):
        res[i] = max(nums[i]+res[i-2], res[i-1])
    return res[-1]
