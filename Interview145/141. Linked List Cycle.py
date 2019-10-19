"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which 
represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Approach 1: Hash Table
Complexity analysis

Time complexity : O(n)O(n). We visit each of the nn elements in the list at most once. 
Adding a node to the hash table costs only O(1)O(1) time.

Space complexity: O(n)O(n). The space depends on the number of elements added to the hash table, 
which contains at most nn elements.

Approach 2: Two Pointers
"""
class Solution(object):
    def hasCycle(self, head):
        nodesSeen = set() # a set is a data type that does not accept duplicates
        while head is not None: # when head is None, you've reached end of linkedlist
            if head in nodesSeen:
                return True
            else:
                nodesSeen.add(head)
            head = head.next # move on to next node
        return False
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None: return False
        fast,slow = head.next,head
        while(fast != slow):
            if fast == None or fast.next == None: return False
            slow = slow.next
            fast = fast.next.next
        return True
        
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return False
        p1 = p2 = head
        
        while True:
            if p1.next != None: p1 = p1.next
            else: break
                
            if p2.next != None and p2.next.next != None: 
                p2 = p2.next.next
            else: break
            
            if p1 == p2:
                return True
        
        return False
