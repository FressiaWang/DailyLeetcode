"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Simple binary search with an additional check.
Comparing target with first element gives us information on witch part of array lies target: 
from begining to max or from min to end. In other words — left or right.
So, when our guess in the middle and our target lies on different sides, we know where to move
"""
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        start = nums[0]
        left, right = 0, len(nums) - 1
        ontheleft = target > start
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right 
        while right - left > 1: # right > left 
            pos = (right + left) // 2
            val = nums[pos]
            if val == target:
                return pos
            if (val > start) != ontheleft:
                if ontheleft :
                    right = pos
                else:
                    left = pos # left = pos + 1
            elif val > target:
                right = pos 
            else:
                left = pos  # left = pos +1
        return -1
"""
I found a very simple and easy understanding solution.

Since the array is sorted and rotated, we just need to make a binary searching.

Somebody may think it is hard because the array is rotated, but it doesn't matter actually!

We just to search it as a 'normal' sorted array.

We split the array into two segments from the middle, one is a normal array and another is rotated.

The we test the target to see which segment it would belongs to.

For a normal segment, which's begin is smaller than the end, the target should be larger than the begin element and less than the end.
For a rotated segment, which's begin is larger than the end, then the target should be larger than the begin element or less than the end.
Recursively split the array and search, finaly we will find out the target.
"""
from typing import List
class Solution:
    def in_range(self, nums: List[int], target: int, i:int, j: int):    
        
        start = nums[i]
        end = nums[j-1]
        
        if start == end:
            return start == target
        elif start < end:
            # normal array
            return start <= target and  target <= end
        else:
		    # rotated array
            return start <= target or target <= end
        
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        
        if j == 0:
            return -1
        
        while i < j:
            pivot = int((i + j) / 2)

            if pivot == i:
                return i if target == nums[i] else -1

            if self.in_range(nums, target, i, pivot):
                j = pivot
            elif self.in_range(nums, target, pivot, j):
                i = pivot
            else:
                return -1
