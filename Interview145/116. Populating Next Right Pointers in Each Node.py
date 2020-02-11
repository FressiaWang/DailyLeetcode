"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer 
should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""
def connect(self, root):
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            #root.right.next = root.next.left if root.next else None
            root = root.next
        root = next
        
def connect1(self, root):
    if root and root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
 
# BFS       
def connect2(self, root):
    if not root:
        return 
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)
    
# DFS 
def connect(self, root):
    if not root:
        return 
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            stack.append(curr.right)
            stack.append(curr.left)
