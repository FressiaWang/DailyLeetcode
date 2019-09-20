"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
https://leetcode.com/problems/next-permutation/solution/
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range((len(nums)-1),0,-1):
            if nums[i-1] < nums[i]:
                for j in range(i,len(nums)+1):
                    if j == len(nums) or nums[j] <= nums[i-1]:
                        nums[j-1], nums[i-1] = nums[i-1], nums[j-1]
                        break
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()
        return
                
