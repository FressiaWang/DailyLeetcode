"""
Sort a linked list in O(n log n) time using constant space complexity.

Method 1 : Merge
Method 2 : QuickSort
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l,r)
    def merge(self,l,r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l,r = r,l
        pre = head = l
        l = l.next
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else :
                pre.next = r
                r = r.next
            pre = pre.next
        pre.next = r or l
        return head
