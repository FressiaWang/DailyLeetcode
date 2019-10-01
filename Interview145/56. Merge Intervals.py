"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
Complexity Analysis

Time complexity : O(n\log{}n)O(nlogn)

Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(nlgn)O(nlgn) 
complexity of sorting.

Space complexity : O(1)O(1) (or O(n)O(n))

If we can sort intervals in place, we do not need more than constant additional space. 
Otherwise, we must allocate linear space to store a copy of intervals and sort that.
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merge = []
        for i in sorted(intervals,key = lambda x : x[0]):
            if not merge or i[0]>merge[-1][1]:
                merge += [i]
            else:
                merge[-1][1] = max(merge[-1][1],i[1])
        return merge
        
