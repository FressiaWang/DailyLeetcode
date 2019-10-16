"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
class Solution(object):
    def flatten(self, root):
        stack = []
        while root or stack:
            # something on left and right. push right node onto stack, swap and move left
            if root.left and root.right:
                stack.append(root.right)
                root.right = root.left
                root.left = None
                root = root.right
            # if just left, then swap and traverse
            elif root.left:
                root.right = root.left
                root.left = None
                root = root.right
            # if just right, then just traverse rightwards
            elif root.right:
                root = root.right
            else:
                if stack:
                    root.right = stack.pop()
                root = root.right
        return

def flatten(self, root):
    nstack = []
    while root:
        if root.left:
            if root.right:
                nstack.append(root.right)
            root.right, root.left = root.left, None
        if not root.right and nstack:
            root.right = nstack.pop()
        root = root.right
def __init__(self):
    self.prev = None
    
def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)
    
    root.right = self.prev
    root.left = None
    self.prev = root
