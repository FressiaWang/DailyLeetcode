"""

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""
def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = root and [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
#recurively
def preorderTraversal(root):
    def dfs(root, ret):
        if root:
            ret.append(root.val)
            dfs(root.left, ret)
            dfs(root.right, ret)
    ret = []
    dfs(root, ret)
    return ret
    
def perorderTraversal(root):
    return [] if not root else [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
