"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

https://github.com/azl397985856/leetcode/blob/master/problems/215.kth-largest-element-in-an-array.md

One solution is to use priority queue to hold k-largest elements. We keep push new element into the pq of size k and pop the minimal one. 
The time complexity is O(nlogk) and space complexity is O(k).

And we can use Python's heapq which is a minimal heap. In the end, we return the top (smallest) element of the pq which is the K's largest number.
Like quick sort, we choose a pivot value and reorder the array as [nums > pivot] + [nums == pivot] + [nums < pivot]. Then we keep D&C the first and third subarray.
Unlike a quick sort, we only need to focus on one subarray in a quick select.
Suppose li and ri is the start index of middle array [nums == pivot] and right array [nums < pivot]:

   	   <p        ==p           >p
    |------|--------------|---------|
   	      (li)           (ri)	 
Thus, if li < k <= ri, the kth largest number falls in middle subarray([nums==pivot]) and we find kth largest number.
Else, if k <= li, the kth largest number falls in left subarray([nums>pivot]) and we D&C in that subarray as sub(left, k).
Else, k > ri, the kth largest number falls in right subarray([nums<pivot]) and we D&C in that subarray as sub(right, k-ri).
"""
def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = nums[:k]
        heapq.heapify(pq)
        for n in nums[k:]:
            heapq.heappush(pq, n)
            heapq.heappop(pq)
        return pq[0]

import random
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        The avarage time of a quick select is O(n). To avoid worst case, we shuffle array in each recursion.
        The quicksort-Partition solution every time we just need to sort half of the remaining list, 
        so the time complexity should be n+n/2+n/4+...=2n, which is O(n).
        快速选择算法的平均时间复杂度是 O(N)，但最坏情况下的时间复杂度是 O(N^2) ，因为我们已经随机选择 pivot，所以能够最大程度上的减少最坏情况发生。
        """
        if not nums: return None
        p = random.choice(nums)
        l = [n for n in nums if n > p]
        m = [n for n in nums if n == p]
        r = [n for n in nums if n < p]
        nums = l + m + r
        i, j = len(l), len(l)+len(m)
        return self.findKthLargest(nums[:i],k) if k <= i else self.findKthLargest(nums[j:],k-j) if k > j else nums[i]

def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pos = self.partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]
 # Lomuto partition scheme   
    def partition(self, nums, l, r):
        index = random.randint(0, len(nums) - 1)
        nums[index], nums[r] = nums[r], nums[index]
        pivot = nums[r]
        lo = l 
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo
