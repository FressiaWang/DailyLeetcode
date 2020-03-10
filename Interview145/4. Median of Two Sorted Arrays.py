"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

Method1:
https://github.com/azl397985856/leetcode/blob/master/problems/4.median-of-two-sorted-array.md
Time complexity is O(log(min(|A|, |B|))) as we binary search within [0, min(|A|, |B|)].
Method2:
https://mp.weixin.qq.com/s/FBlH7o-ssj_iMEPLcvsY2w
"""
def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            l1, l2, nums1, nums2 = l2, l1, nums2, nums1
        l, r = 0, l1
        while l <= r:
            i = l + r >> 1
            j = (l1 + l2 + 1 >> 1) - i
            if i > 0 and nums1[i-1] > nums2[j]: r = i - 1
            elif i < l1 and nums1[i] < nums2[j-1]: l = i + 1
            else:
                left = max(nums1[i-1], nums2[j-1]) if i*j else nums2[j-1] if j else nums1[i-1]
                if l1 + l2 & 1: return left/1.0
                right = nums1[i] if j == l2 else nums2[j] if i == l1 else min(nums1[i], nums2[j])
                return (left + right)/2.0

def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        
        left_size = (m + n + 1) // 2
        start = 0
        end = m
        is_even = ((m + n) % 2) == 0
        while start <= end:
            a_part = (start + end) // 2
            b_part = left_size - a_part
            
            aleftmax = float("-inf") if a_part == 0 else nums1[a_part - 1]
            arightmin = float("inf") if a_part == m else nums1[a_part]
            bleftmax = float("-inf") if b_part == 0 else nums2[b_part - 1]
            brightmin = float("inf") if b_part == n else nums2[b_part]
            
            if aleftmax <= brightmin and bleftmax <= arightmin:
                if not is_even:
                    return max(aleftmax, bleftmax)
                else:
                    return (max(aleftmax, bleftmax) + min(arightmin, brightmin))/ 2
            elif aleftmax > brightmin:
                end = a_part - 1
            elif bleftmax > arightmin:
                start = a_part + 1
                
def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2: return self.findKthsmallest(nums1, nums2, l//2+1)
        else: return (self.findKthsmallest(nums1, nums2, l//2)+self.findKthsmallest(nums1, nums2, l//2+1))/2.0
        
    def findKthsmallest(self, nums1, nums2, k):
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        if not nums1: return nums2[k-1]
        if k == 1: return min(nums1[0], nums2[0])
        pa = min(k//2,len(nums1))
        pb = k-pa
        if nums1[pa-1] <= nums2[pb-1]:
            return self.findKthsmallest(nums1[pa:],nums2,k-pa)
        else:
            return self.findKthsmallest(nums1, nums2[pb:],k-pb)                
