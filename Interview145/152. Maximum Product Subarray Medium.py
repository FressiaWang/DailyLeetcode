"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray

Maximum Subarray那题的变种。由于正负得负，负负得正的关系。以A[i]结尾的max product subarray同时取决于以A[i-1]
结尾的max / min product subarray以及A[i]本身。因此，对每个i，需要记录min/max product两个状态：

max_product[i] = max(max_product[i-1]*A[i], min_product[i-1]*A[i], A[i]) 
min_product[i] = min(max_product[i-1]*A[i], min_product[i-1]*A[i], A[i]) 
"""
def maxProduct(self, nums):
    if not nums:
        return 
    locMin = locMax = gloMax = nums[0]
    for i in xrange(1, len(nums)):
        tmp = locMin
        locMin = min(locMin*nums[i], nums[i], locMax*nums[i])
        locMax = max(tmp*nums[i], nums[i], locMax*nums[i])
        gloMax = max(gloMax, locMax)
    return gloMax
