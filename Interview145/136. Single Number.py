"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

Approach 2: Hash Table
Algorithm

We use hash table to avoid the O(n)O(n) time required for searching the elements.

Iterate through all elements in \text{nums}nums
Try if hash\_tablehash_table has the key for pop
If not, set up key/value pair
In the end, there is only one element in hash\_tablehash_table, so use popitem to get it

Complexity Analysis

Time complexity : O(n \cdot 1) = O(n)O(n⋅1)=O(n). Time complexity of for loop is O(n)O(n). 
Time complexity of hash table(dictionary in python) operation pop is O(1)O(1).

Space complexity : O(n)O(n). The space required by hash\_tablehash_table is equal to the number of elements in \text{nums}nums

Approach 3: Math
Concept

2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c

Complexity Analysis

Time complexity : O(n + n) = O(n)O(n+n)=O(n). sum will call next to iterate through \text{nums}nums. 
We can see it as sum(list(i, for i in nums)) which means the time complexity is O(n)O(n) because of the number
of elements(nn) in \text{nums}nums.

Space complexity : O(n + n) = O(n)O(n+n)=O(n). set needs space for the elements in nums
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
        
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
