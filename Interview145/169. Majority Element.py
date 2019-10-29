"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Approach 2: HashMap
Time complexity : O(n)O(n)

We iterate over nums once and make a constant time HashMap insertion on each iteration. Therefore, the algorithm runs in O(n)O(n) time.

Space complexity : O(n)O(n)
Approach 3: Sorting
Time complexity : O(nlgn)O(nlgn)

Sorting the array costs O(nlgn)O(nlgn) time in Python and Java, so it dominates the overall runtime.

Space complexity : O(1)O(1) or (O(n)O(n))

We sorted nums in place here - if that is not allowed, then we must spend linear additional space on 
a copy of nums and sort the copy instead.
Approach 5: Divide and Conquer
Time complexity : O(nlgn)O(nlgn)Space complexity : O(lgn)O(lgn)

Approach 6: Boyer-Moore Voting Algorithm
Complexity Analysis

Time complexity : O(n)O(n)

Boyer-Moore performs constant work exactly nn times, so the algorithm runs in linear time.

Space complexity : O(1)O(1)

Boyer-Moore allocates only constant additional memory.
"""
def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
        
def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
