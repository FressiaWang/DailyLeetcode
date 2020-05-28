"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution(object):
def findMin(self, nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo] 

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        l, r = 0, len(nums)-1
        if nums[l] <= nums[r]: 
            return nums[l]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            else:
                return nums[r]
