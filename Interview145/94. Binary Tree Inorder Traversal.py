"""
Given a binary tree, return the inorder traversal of its nodes' values.
Complexity Analysis

Time complexity : O(n)O(n).

Space complexity : O(n)O(n).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res,stack = [],[]
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            c = stack.pop()
            res.append(c.val)
            if c.right:
                p = c.right
        return res
