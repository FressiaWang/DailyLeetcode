"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
def pathSum1(self, root, sum):
    res = []
    self.dfs(root, sum, [], res)
    return res
    
def dfs(self, root, sum, path, res):
    if root:
        if sum == root.val and not root.left and not root.right:
            res.append(path+[root.val])
        self.dfs(root.left, sum-root.val, path+[root.val], res)
        self.dfs(root.right, sum-root.val, path+[root.val], res)
        
def pathSum2(self, root, sum):
    res, stack = [], [(root, sum, [])]
    while stack:
        node, sum, path = stack.pop()
        if node:
            if node.val == sum and not node.left and not node.right:
                res.append(path+[node.val])
            stack.append((node.right, sum-node.val, path+[node.val]))
            stack.append((node.left, sum-node.val, path+[node.val]))
    return res
