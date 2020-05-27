"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        rootValue = preorder.pop(0)
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)
        root.left = self.buildTree(preorder,inorder[:inorderIndex])
        root.right = self.buildTree(preorder,inorder[inorderIndex+1:])
        return root
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
            
        head = TreeNode(preorder[0])
        stack = [head]
        i = 1
        j = 0
        
        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1
        
        return head
