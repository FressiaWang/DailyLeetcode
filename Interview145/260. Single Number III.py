"""
260. Single Number III
Medium

1349

97

Add to List

Share
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for n in nums:
            xor ^= n
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        first, second = 0, 0
        for n in nums:
            if n & mask == 0:
                first ^= n
            else:
                second ^= n
        return [first, second]
