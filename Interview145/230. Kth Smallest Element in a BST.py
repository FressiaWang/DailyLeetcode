"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Time complexity : \mathcal{O}(H + k)O(H+k), where HH is a tree height. This complexity is defined by the stack,
which contains at least H + kH+k elements, since before starting to pop out one has to go down to a leaf. 
This results in \mathcal{O}(\log N + k)O(logN+k) for the balanced tree and \mathcal{O}(N + k)O(N+k) for 
completely unbalanced tree with all the nodes in the left subtree.
Space complexity : \mathcal{O}(H + k)O(H+k), the same as for time complexity, \mathcal{O}(N + k)O(N+k) in the worst case, 
and \mathcal{O}(\log N + k)O(logN+k) in the average case.
"""
def kthSmallest(self, root, k):
    self.k = k
    self.res = None
    self.helper(root)
    return self.res

def helper(self, node):
    if not node:
        return
    self.helper(node.left)
    self.k -= 1
    if self.k == 0:
        self.res = node.val
        return
    self.helper(node.right)


def kthSmallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
