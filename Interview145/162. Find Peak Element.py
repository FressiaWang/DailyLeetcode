"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

Approach 1: Linear Scan
In this approach, we make use of the fact that two consecutive numbers nums[j]nums[j] and nums[j + 1]nums[j+1] are never equal.
Thus, we can traverse over the numsnums array starting from the beginning. Whenever, we find a number nums[i]nums[i], 
we only need to check if it is larger than the next number nums[i+1]nums[i+1] for determining if nums[i]nums[i] is the 
peak element. The reasoning behind this can be understood by taking the following three cases which cover every case into 
which any problem can be divided.
Case 1. All the numbers appear in a descending order. In this case, the first element corresponds to the peak element. 
We start off by checking if the current element is larger than the next one. The first element satisfies this criteria, 
and is hence identified as the peak correctly. In this case, we didn't reach a point where we needed to compare nums[i]
nums[i] with nums[i-1]nums[i−1] also, to determine if it is the peak element or not.
Case 2. All the elements appear in ascending order. In this case, we keep on comparing nums[i]nums[i] with nums[i+1]nums[i+1] 
to determine if nums[i]nums[i] is the peak element or not. None of the elements satisfy this criteria, indicating that 
we are currently on a rising slope and not on a peak. Thus, at the end, we need to return the last element as the peak element,
which turns out to be correct. In this case also, we need not compare nums[i]nums[i] with nums[i-1]nums[i−1], 
since being on the rising slope is a sufficient condition to ensure that nums[i]nums[i] isn't the peak element.
Case 3. The peak appears somewhere in the middle. In this case, when we are traversing on the rising edge, as in Case 2,
none of the elements will satisfy nums[i] > nums[i + 1]nums[i]>nums[i+1]. We need not compare nums[i]nums[i] with 
nums[i-1]nums[i−1] on the rising slope as discussed above. When we finally reach the peak element, 
the condition nums[i] > nums[i + 1]nums[i]>nums[i+1] is satisfied. We again, need not compare nums[i]nums[i] with 
nums[i-1]nums[i−1]. This is because, we could reach nums[i]nums[i] as the current element only when the check 
nums[i] > nums[i + 1]nums[i]>nums[i+1] failed for the previous((i-1)^{th}(i−1) 
the element, indicating that nums[i-1] < nums[i]nums[i−1]<nums[i]. Thus, we are able to identify the peak element 
correctly in this case as well.

Approach 3: Iterative Binary Search
To see how it works, let's consider the three cases discussed above again.

Case 1. In this case, we firstly find 33 as the middle element. Since it lies on a falling slope, we reduce the search space 
to [1, 2, 3]. For this subarray, 22 happens to be the middle element, which again lies on a falling slope, reducing the search
space to [1, 2]. Now, 11 acts as the middle element and it lies on a falling slope, reducing the search space to [1] only. 
Thus, 11 is returned as the peak correctly.
Case 2. In this case, we firstly find 33 as the middle element. Since it lies on a rising slope, we reduce the search space
to [4, 5]. Now, 44 acts as the middle element for this subarray and it lies on a rising slope, reducing the search space to 
[5] only. Thus, 55 is returned as the peak correctly.
Case 3. In this case, the peak lies somewhere in the middle. The first middle element is 44. It lies on a rising slope, 
indicating that the peak lies towards its right. Thus, the search space is reduced to [5, 1]. Now, 55 happens to be the on 
a falling slope(relative to its right neighbour), reducing the search space to [5] only. Thus, 55 is identified as the peak 
element correctly.
"""
def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
        
