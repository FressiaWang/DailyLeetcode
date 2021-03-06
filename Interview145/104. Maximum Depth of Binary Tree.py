"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            child_level = []
            for lef in level:
                if lef.left:
                    child_level.append(lef.left)
                if lef.right:
                    child_level.append(lef.right)
            level = child_level
        return depth
def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        p = root and deque([(root, 1)])
        d = 0
        while p:
            node, d = p.popleft()
            if node.left:
                p.append((node.left, d+1))
            if node.right:
                p.append((node.right, d+1))
        return d
def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
