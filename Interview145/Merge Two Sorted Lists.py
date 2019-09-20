"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        head = ListNode(0)
        head.next = l3
        while l1 and l2:
            if (l1.val < l2.val):
                l3.next = l1
                l1 = l1.next
            else: 
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 or l2
        return head.next.next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)

        head = l3
        while l1 or l2:
            if l1 and l2:
                l1, l2 = (l1,l2) if l1.val < l2.val else (l2,l1)
                l3.next = l1
                l1 = l1.next
                l3= l3.next
            else:
                l3.next = l1 or l2
                l1,l2 = None,None

        return head.next
