"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right = 0,len(nums)-1
        while right > left:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return [self.left_most(nums,0,mid,target),self.right_most(nums,mid,len(nums)-1,target)]
        return [-1,-1]
    def left_most(self,nums,left,right,target):
        while right > left:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid-1] < target:
                return mid
            else: right = mid-1
        return left
    def right_most(self,nums,left,right,target):
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid+1] > target:
                return mid
            else: left = mid + 1
        return right
