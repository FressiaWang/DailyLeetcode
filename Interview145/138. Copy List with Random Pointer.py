"""
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, 
or null if it does not point to any node.
https://www.cnblogs.com/zuoyuan/p/3745126.html
"""
def copyRandomList1(self, head):
    if not head:
        return 
    # copy nodes
    cur = head
    while cur:
        nxt = cur.next
        cur.next = Node(cur.val)
        cur.next.next = nxt
        cur = nxt
    # copy random pointers
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    # separate two parts
    second = cur = head.next
    while cur.next:
        head.next = cur.next
        head = head.next
        cur.next = head.next
        cur = cur.next
    head.next = None
    return second

# using dictionary    
def copyRandomList(self, head):
    if not head:
        return 
    cur, dic = head, {}
    # copy nodes
    while cur:
        dic[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    # copy random pointers
    while cur:
        if cur.random:
            dic[cur].random = dic[cur.random]
        if cur.next:
            dic[cur].next = dic[cur.next]
        cur = cur.next
    return dic[head]
