"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
https://www.youtube.com/watch?v=MRe3UsRadKw
"""
class Solution(object):        
    def reverseList(self, head):  # Iterative  O(n) Time / O(1) Space
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        
    def reverseList(self, head):  # Recursive  O(n) Time / O(n) Space
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p 
