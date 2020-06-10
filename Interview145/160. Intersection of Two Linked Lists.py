"""
Write a program to find the node at which the intersection of two singly linked lists begins.
If two linked lists have intersection, we can find two observations:

They must have same nodes after the intersection point.
L1+L2 must have same tail from the intersection point as L2 + L1. For example,
L1 = 1,2,3
L2 = 6,5,2,3

L1+L2 = 1,2,3,6,5,2,3
L2+L1 = 6,5,2,3,1,2,3

To implement L1+L2 as well as L2+L1, we can simply jump to another list's head
after traveling through certain list.
But, you need to notice that if the two lists have no intersection at all,
you should stop after you've already checked L1+L2, so we need a flag jumpToNext to ensure we only traverse L1 + L2 once.
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA, pB, jumpNext = headA, headB, False
        while pA and pB:
            if pA == pB:
                return pA
            pA, pB = pA.next, pB.next
            if not pA and not jumpNext:
                pA, jumpNext = headB, True
            if not pB:
                pB = headA
        return None
def getIntersectionNode(self, headA, headB):
    p1, p2 = headA, headB
    while p1 is not p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1
